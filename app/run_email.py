"""IMAP-клиент для Telegram-бота.

Главные отличия от исходной версии:
- Все операции с письмами идут через UID (``mail.uid(...)``), а не через
  sequence numbers. Раньше ``get_unseen`` использовал ``mail.search``,
  сохранял sequence numbers в кэш как ``uid``, а ``get_message`` потом звал
  ``mail.uid("FETCH", uid)`` — UIDs и sequence numbers не совпадают,
  поэтому чтение писем ломалось на любом ящике, где они расходятся.
- ``MailClient`` теперь контекстный менеджер (``with MailClient() as mail:``),
  гарантирующий закрытие соединения даже при исключении.
- ``connect()`` логирует ошибки и пробрасывает человекочитаемые исключения.
- ``get_unseen`` использует ``BODY.PEEK[HEADER.FIELDS (...)]`` — забираем
  только нужные заголовки, экономим трафик и не помечаем письмо прочитанным.
- ``get_attachments`` принимает опциональный ``folder`` (по умолчанию
  ``MAIL_FOLDER``) — это фиксит баг в ``file_handler``, который звал метод
  без папки.
- ``search_orders`` безопасно обрабатывает пустой ответ сервера
  (``data[0] is None``).
- Везде тип-аннотации и ``logging`` вместо ``print``.
"""

from __future__ import annotations

import base64
import email
import imaplib
import logging
from email.header import decode_header
from email.message import Message
from email.utils import parseaddr
from typing import Iterable, Optional

from config import EMAIL, PASSWORD, IMAP_SERVER, IMAP_PORT, ORDER_EMAIL, MAIL_FOLDER

logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# IMAP UTF-7 (RFC 3501, раздел 5.1.3)
# ----------------------------------------------------------------------

def decode_imap_utf7(s: str) -> str:
    """Декодирование имён папок IMAP UTF-7."""
    result: list[str] = []
    i = 0
    while i < len(s):
        if s[i] == "&":
            end = s.find("-", i)
            if end == -1:
                end = len(s)
            encoded = s[i + 1:end]
            if encoded:
                encoded = encoded.replace(",", "/")
                decoded = base64.b64decode(encoded + "=" * (-len(encoded) % 4))
                result.append(decoded.decode("utf-16-be"))
            else:
                result.append("&")
            i = end + 1
        else:
            result.append(s[i])
            i += 1
    return "".join(result)


def encode_imap_utf7(s: str) -> str:
    """Кодирование имени папки в IMAP UTF-7."""
    result: list[str] = []
    buffer: list[str] = []

    def flush_buffer() -> str:
        if not buffer:
            return ""
        encoded = "".join(buffer).encode("utf-16-be")
        encoded = base64.b64encode(encoded).decode().rstrip("=").replace("/", ",")
        buffer.clear()
        return "&" + encoded + "-"

    for ch in s:
        if 0x20 <= ord(ch) <= 0x7E:
            result.append(flush_buffer())
            result.append(ch)
        else:
            buffer.append(ch)
    result.append(flush_buffer())
    return "".join(result)


# ----------------------------------------------------------------------
# Исключения
# ----------------------------------------------------------------------

class MailError(Exception):
    """Базовая ошибка почтового клиента."""


class MailConnectionError(MailError):
    """Не удалось подключиться/аутентифицироваться."""


# ----------------------------------------------------------------------
# Клиент
# ----------------------------------------------------------------------

class MailClient:
    """Тонкая обёртка над :class:`imaplib.IMAP4_SSL`.

    Использовать предпочтительно через ``with``::

        with MailClient() as mail:
            letters = mail.get_unseen()
    """

    IMAP_TIMEOUT = 30

    def __init__(
        self,
        server: str = IMAP_SERVER,
        port: int = IMAP_PORT,
        email_addr: str = EMAIL,
        password: str = PASSWORD,
    ) -> None:
        self._server = server
        self._port = port
        self._email = email_addr
        self._password = password
        self.mail: Optional[imaplib.IMAP4_SSL] = None

    # --- контекстный менеджер -------------------------------------------

    def __enter__(self) -> "MailClient":
        self.connect()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.disconnect()

    # --- подключение ----------------------------------------------------

    def connect(self) -> None:
        """Подключение и аутентификация на IMAP-сервере."""
        try:
            self.mail = imaplib.IMAP4_SSL(self._server, self._port)
            self.mail._encoding = "utf-8"  # noqa: SLF001 — приватный атрибут imaplib
            self.mail.login(self._email, self._password)
            self.mail.select("INBOX")
        except imaplib.IMAP4.error as e:
            logger.exception("IMAP connection error")
            raise MailConnectionError(f"Не удалось подключиться к почте: {e}") from e
        logger.debug("IMAP connected as %s", self._email)

    def disconnect(self) -> None:
        """Корректное закрытие соединения."""
        if self.mail is not None:
            try:
                self.mail.logout()
            except imaplib.IMAP4.error:
                logger.warning("IMAP logout error (ignoring)", exc_info=True)
            finally:
                self.mail = None

    # --- папки ----------------------------------------------------------

    def select_folder(self, folder: str) -> bool:
        """Выбор папки с кодированием IMAP UTF-7."""
        if self.mail is None:
            raise MailError("MailClient не подключён")
        folder_utf7 = encode_imap_utf7(folder)
        status, _ = self.mail.select(f'"{folder_utf7}"')
        return status == "OK"

    def show_folders(self) -> list[str]:
        """Список имён папок (декодированных)."""
        if self.mail is None:
            raise MailError("MailClient не подключён")
        status, folders = self.mail.list()
        if status != "OK":
            return []
        names: list[str] = []
        for folder in folders:
            line = folder.decode() if isinstance(folder, bytes) else folder
            # берём последнее имя в кавычках
            parts = line.split('"')
            if len(parts) >= 2:
                names.append(decode_imap_utf7(parts[-2]))
        return names

    # --- декодирование заголовков --------------------------------------

    @staticmethod
    def decode_header_value(value: Optional[str]) -> str:
        if not value:
            return ""
        result: list[str] = []
        for text, encoding in decode_header(value):
            if isinstance(text, bytes):
                result.append(text.decode(encoding or "utf-8", errors="replace"))
            else:
                result.append(text)
        return "".join(result)

    # --- получение писем ------------------------------------------------

    def get_unseen(self) -> list[dict]:
        """Список непрочитанных писем из INBOX.

        UID сохраняется в поле ``uid`` и дальше используется во всех
        операциях через ``mail.uid(...)``.
        """
        if self.mail is None:
            raise MailError("MailClient не подключён")

        status, data = self.mail.uid("SEARCH", None, "UNSEEN")
        if status != "OK" or not data or not data[0]:
            return []

        uids = data[0].split()
        letters: list[dict] = []

        for uid in reversed(uids):
            # Берём только нужные заголовки — быстрее и не помечает письмо
            # прочитанным благодаря PEEK.
            status, msg_data = self.mail.uid(
                "FETCH",
                uid,
                "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)])",
            )
            if status != "OK":
                continue

            msg = email.message_from_bytes(msg_data[0][1])

            sender_name, sender_email = parseaddr(msg.get("From", ""))
            sender_name = self.decode_header_value(sender_name).strip().strip('"')
            subject = self.decode_header_value(msg.get("Subject", ""))

            letters.append({
                "uid": uid.decode(),
                "folder": "INBOX",
                "sender_name": sender_name,
                "sender_email": sender_email,
                "subject": subject,
            })

        logger.debug("get_unseen: %d letter(s)", len(letters))
        return letters

    def get_message(self, uid: str, folder: str = MAIL_FOLDER) -> Optional[Message]:
        """Получение полного тела письма по UID."""
        if self.mail is None:
            raise MailError("MailClient не подключён")

        folder_utf7 = encode_imap_utf7(folder)
        status, _ = self.mail.select(f'"{folder_utf7}"')
        if status != "OK":
            logger.error("Не удалось открыть папку %r", folder)
            return None

        if isinstance(uid, str):
            uid_b = uid.encode()
        else:
            uid_b = uid

        status, msg_data = self.mail.uid("FETCH", uid_b, "(BODY.PEEK[])")
        if status != "OK":
            logger.error("FETCH failed for uid=%s", uid)
            return None

        for item in msg_data:
            if isinstance(item, tuple):
                return email.message_from_bytes(item[1])
        return None

    def get_text(self, uid: str, folder: str = MAIL_FOLDER) -> str:
        """Извлечение текста письма (plain предпочтительнее html)."""
        msg = self.get_message(uid, folder)
        if not msg:
            return "Не удалось получить письмо"

        text_plain = ""
        text_html = ""

        if msg.is_multipart():
            for part in msg.walk():
                disposition = str(part.get("Content-Disposition", ""))
                if "attachment" in disposition.lower():
                    continue
                content_type = part.get_content_type()
                payload = part.get_payload(decode=True)
                if not payload:
                    continue
                charset = part.get_content_charset() or "utf-8"
                try:
                    body = payload.decode(charset, errors="replace")
                except (LookupError, UnicodeDecodeError):
                    body = payload.decode("utf-8", errors="replace")
                if content_type == "text/plain" and not text_plain:
                    text_plain = body
                elif content_type == "text/html" and not text_html:
                    text_html = body
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                charset = msg.get_content_charset() or "utf-8"
                text_plain = payload.decode(charset, errors="replace")

        if text_plain.strip():
            return text_plain.strip()

        if text_html.strip():
            from html import unescape
            import re
            text = re.sub(r"<[^>]+>", "", text_html)
            return unescape(text).strip()

        return "Письмо не содержит текста"

    def get_attachments(
        self,
        uid: str,
        folder: str = MAIL_FOLDER,
    ) -> list[dict]:
        """Список вложений письма по UID.

        ``folder`` теперь опциональный (дефолт ``MAIL_FOLDER``) — это
        фиксит баг в ``file_handler``, который звал метод без папки.
        """
        msg = self.get_message(uid, folder)
        if not msg:
            return []

        files: list[dict] = []
        for part in msg.walk():
            disposition = part.get("Content-Disposition", "")
            if "attachment" not in disposition.lower():
                continue
            filename = part.get_filename()
            if not filename:
                continue
            filename = self.decode_header_value(filename)
            data = part.get_payload(decode=True)
            if data:
                files.append({"filename": filename, "data": data})
        return files

    def search_orders(self, number: str) -> list[dict]:
        """Поиск писем с заказом ``number`` от ``ORDER_EMAIL`` в ``MAIL_FOLDER``.

        Безопасно обрабатывает пустой ответ сервера (``data[0] is None``).
        """
        if self.mail is None:
            raise MailError("MailClient не подключён")

        folder_utf7 = encode_imap_utf7(MAIL_FOLDER)
        status, _ = self.mail.select(f'"{folder_utf7}"')
        if status != "OK":
            logger.error("Не удалось открыть папку %r", MAIL_FOLDER)
            return []

        # Экранируем кавычки в номере — он может прийти от пользователя.
        safe_number = number.replace('"', '')
        criteria = f'FROM "{ORDER_EMAIL}" SUBJECT "Заказ {safe_number}"'
        logger.debug("IMAP search: %s", criteria)

        status, data = self.mail.uid("SEARCH", None, criteria)
        if status != "OK" or not data or not data[0]:
            return []

        result: list[dict] = []
        for uid in data[0].split():
            status, msg_data = self.mail.uid(
                "FETCH",
                uid,
                "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)])",
            )
            if status != "OK":
                continue

            msg = email.message_from_bytes(msg_data[0][1])
            subject = self.decode_header_value(msg.get("Subject", ""))
            sender_name, sender_email = parseaddr(msg.get("From", ""))

            result.append({
                "uid": uid.decode(),
                "folder": MAIL_FOLDER,
                "sender_name": self.decode_header_value(sender_name),
                "sender_email": sender_email,
                "subject": subject,
            })

        logger.debug("search_orders(%r): %d hit(s)", number, len(result))
        return result
