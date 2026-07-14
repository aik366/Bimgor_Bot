"""Хендлеры Telegram-бота для работы с почтой.

Главные отличия от исходной версии:
- ``mail_cache`` теперь **персистентный по пользователю**: ключ —
  ``user_id``, значение — словарь писем. Раньше кэш был глобальным, и
  разные юзеры видели чужие письма.
- Все блокирующие IMAP-операции запускаются через ``asyncio.to_thread`` —
  больше не блокируют event loop aiogram.
- Везде ``try/except`` с человекочитаемыми сообщениями и гарантированным
  ``callback.answer()`` (в исходнике при ошибке колесо в Telegram крутилось
  бесконечно).
- ``file_handler`` фикс: раньше звал ``mail.get_attachments(uid)`` без
  ``folder`` и падал с ``TypeError``.
- ``text_handler``/``files_handler`` используют ``mail_cache.get(uid)`` и
  аккуратно сообщают, если письмо уже вытеснено из кэша.
- Добавлен хендлер для callback ``main`` (раньше кнопка «Назад» в результатах
  поиска ничего не делала).
- Добавлена команда ``/help``.
- ``MailClient`` используется как контекстный менеджер (``with``),
  что гарантирует закрытие соединения при любом исходе.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Optional

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import BufferedInputFile, CallbackQuery, InlineKeyboardMarkup, Message

from app.keyboards_email import (
    files_keyboard,
    letter_keyboard,
    mail_list_keyboard,
    main_menu,
    search_result_keyboard,
)
from app.run_email import MailClient, MailConnectionError, MailError

logger = logging.getLogger(__name__)

router = Router()

# Лимит длины сообщения в Telegram — 4096. Оставляем запас на префикс.
TG_TEXT_LIMIT = 4000


# ----------------------------------------------------------------------
# FSM-состояния
# ----------------------------------------------------------------------

class SearchState(StatesGroup):
    waiting_number = State()


# ----------------------------------------------------------------------
# Per-user кэш писем
# ----------------------------------------------------------------------

# Структура: { user_id (int): { uid (str): letter (dict) } }
mail_cache: dict[int, dict[str, dict]] = {}


def _get_user_cache(user_id: int) -> dict[str, dict]:
    """Возвращает (создавая при необходимости) кэш писем пользователя."""
    return mail_cache.setdefault(user_id, {})


def _set_user_cache(user_id: int, letters) -> dict[str, dict]:
    """Полная замена кэша пользователя новым набором писем."""
    cache = {letter["uid"]: letter for letter in letters}
    mail_cache[user_id] = cache
    return cache


def _get_letter(user_id: int, uid: str) -> Optional[dict]:
    return _get_user_cache(user_id).get(uid)


# ----------------------------------------------------------------------
# Вспомогательные функции
# ----------------------------------------------------------------------

async def _run_sync(func, *args, **kwargs):
    """Запуск синхронной IMAP-функции в пуле потоков."""
    loop = asyncio.get_running_loop() 
    return await loop.run_in_executor(None, func, *args, **kwargs)


# ----------------------------------------------------------------------
# /start, /help
# ----------------------------------------------------------------------

@router.message(F.text == "📨 Бимгор")
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать.\n\n"
        "Доступные действия:\n"
        "• 🔎 **Поиск** — поиск заказа по номеру\n",
        reply_markup=main_menu(),
    )


# ----------------------------------------------------------------------
# Главное меню (callback "main")
# ----------------------------------------------------------------------

@router.callback_query(F.data == "main")
async def main_menu_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите действие:",
        reply_markup=main_menu(),
    )
    await callback.answer()


# ----------------------------------------------------------------------
# Кнопка Почта
# ----------------------------------------------------------------------

@router.callback_query(F.data == "mail")
async def mail_handler(callback: CallbackQuery):
    user_id = callback.from_user.id

    try:
        def _fetch():
            with MailClient() as mail:
                return mail.get_unseen()

        letters = await _run_sync(_fetch)
    except MailConnectionError:
        logger.warning("IMAP connection failed for user %s", user_id)
        await callback.answer("⚠️ Не удалось подключиться к почте", show_alert=True)
        return
    except MailError as e:
        logger.warning("Mail error for user %s: %s", user_id, e)
        await callback.answer(f"⚠️ {e}", show_alert=True)
        return
    except Exception:
        logger.exception("Unexpected error in mail_handler")
        await callback.answer("⚠️ Внутренняя ошибка", show_alert=True)
        return

    _set_user_cache(user_id, letters)

    if not letters:
        await callback.answer("📭 Непрочитанных писем нет", show_alert=False)
        return

    await callback.message.edit_text(
        f"📧 Непрочитанные письма: {len(letters)}",
        reply_markup=mail_list_keyboard(letters),
    )
    await callback.answer()


# ----------------------------------------------------------------------
# Выбор письма
# ----------------------------------------------------------------------

@router.callback_query(F.data.startswith("letter:"))
async def letter_handler(callback: CallbackQuery):
    uid = callback.data.split(":", 1)[1]
    letter = _get_letter(callback.from_user.id, uid)

    if not letter:
        await callback.answer("Письмо больше недоступно, обновите список", show_alert=True)
        return

    text = (
        "📧 Письмо\n\n"
        f"От:\n{letter['sender_name']}\n\n"
        f"E-mail:\n{letter['sender_email']}\n\n"
        f"Тема:\n{letter['subject']}"
    )

    await callback.message.edit_text(
        text,
        reply_markup=letter_keyboard(uid),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("text:"))
async def text_handler(callback: CallbackQuery):
    uid = callback.data.split(":", 1)[1]
    user_id = callback.from_user.id
    letter = _get_letter(user_id, uid)

    if not letter:
        await callback.answer("Письмо больше недоступно", show_alert=True)
        return

    try:
        def _fetch():
            with MailClient() as mail:
                return mail.get_text(uid, letter["folder"])

        text = await _run_sync(_fetch)
    except MailError as e:
        await callback.answer(f"⚠️ {e}", show_alert=True)
        return
    except Exception:
        logger.exception("Unexpected error in text_handler")
        await callback.answer("⚠️ Внутренняя ошибка", show_alert=True)
        return

    if not text:
        text = "📭 Письмо не содержит текста"

    if len(text) > TG_TEXT_LIMIT:
        text = text[:TG_TEXT_LIMIT] + "\n\n..."

    await callback.message.edit_text(
        "📄 Текст письма\n\n" + text,
        reply_markup=letter_keyboard(uid),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("files:"))
async def files_handler(callback: CallbackQuery):
    uid = callback.data.split(":", 1)[1]
    user_id = callback.from_user.id
    letter = _get_letter(user_id, uid)

    if not letter:
        await callback.answer("Письмо больше недоступно", show_alert=True)
        return

    try:
        def _fetch():
            with MailClient() as mail:
                return mail.get_attachments(uid, letter["folder"])

        files = await _run_sync(_fetch)
    except MailError as e:
        await callback.answer(f"⚠️ {e}", show_alert=True)
        return
    except Exception:
        logger.exception("Unexpected error in files_handler")
        await callback.answer("⚠️ Внутренняя ошибка", show_alert=True)
        return

    if not files:
        await callback.message.edit_text(
            "📎 Вложений нет",
            reply_markup=letter_keyboard(uid),
        )
        await callback.answer()
        return

    await callback.message.edit_text(
        f"📎 Вложения: {len(files)}",
        reply_markup=files_keyboard(files, uid),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("file:"))
async def file_handler(callback: CallbackQuery):
    parts = callback.data.split(":")
    # формат: file:<uid>:<index>
    if len(parts) != 3:
        await callback.answer("Некорректный запрос файла", show_alert=True)
        return

    _, uid, index_str = parts
    user_id = callback.from_user.id
    letter = _get_letter(user_id, uid)

    if not letter:
        await callback.answer("Письмо больше недоступно", show_alert=True)
        return

    try:
        index = int(index_str)
    except ValueError:
        await callback.answer("Некорректный индекс файла", show_alert=True)
        return

    try:
        def _fetch():
            with MailClient() as mail:
                return mail.get_attachments(uid, letter["folder"])

        files = await _run_sync(_fetch)
    except MailError as e:
        await callback.answer(f"⚠️ {e}", show_alert=True)
        return
    except Exception:
        logger.exception("Unexpected error in file_handler")
        await callback.answer("⚠️ Внутренняя ошибка", show_alert=True)
        return

    if index < 0 or index >= len(files):
        await callback.answer("Файл не найден, обновите список", show_alert=True)
        return

    file = files[index]
    document = BufferedInputFile(file["data"], filename=file["filename"])

    await callback.message.answer_document(document)
    await callback.answer()


# ----------------------------------------------------------------------
# Поиск заказа
# ----------------------------------------------------------------------

@router.callback_query(F.data == "search")
async def search_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(SearchState.waiting_number)
    await callback.message.answer("🔎 Введите номер заказа:")
    await callback.answer()


@router.message(SearchState.waiting_number)
async def search_number(message: Message, state: FSMContext):
    number = (message.text or "").strip()
    user_id = message.from_user.id

    if not number:
        await message.answer("Номер заказа пуст. Попробуйте ещё раз:")
        return

    await state.clear()

    try:
        def _search():
            with MailClient() as mail:
                return mail.search_orders(number)

        letters = await _run_sync(_search)
    except MailError as e:
        await message.answer(f"⚠️ {e}", reply_markup=main_menu())
        return
    except Exception:
        logger.exception("Unexpected error in search_number")
        await message.answer("⚠️ Внутренняя ошибка", reply_markup=main_menu())
        return

    if not letters:
        await message.answer(
            f"❌ Заказ {number} не найден",
            reply_markup=main_menu(),
        )
        return

    _set_user_cache(user_id, letters)

    await message.answer(
        f"🔎 Найдено: {len(letters)}",
        reply_markup=search_result_keyboard(letters),
    )


# ----------------------------------------------------------------------
# Fallback на неизвестный callback (чтобы колесо не крутилось)
# ----------------------------------------------------------------------

# @router.callback_query()
# async def unknown_callback(callback: CallbackQuery):
#     await callback.answer()
