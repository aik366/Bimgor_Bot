"""Inline-клавиатуры бота.

Изменения относительно исходника:
- Удалён дублирующий импорт ``InlineKeyboardBuilder`` (был дважды).
- Добавлены тип-аннотации.
- ``mail_list_keyboard`` теперь ограничивает длину имени отправителя
  (Telegram обрезает длинные кнопки, но лучше сделать это осмысленно).
- ``search_result_keyboard`` тем же способом ограничивает длину темы.
- ``files_keyboard`` ограничивает длину имени файла.
"""

from __future__ import annotations

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup

# Telegram обрезает надписи кнопок ~ до 64 байт, ориентируемся на 40 символов.
BUTTON_TEXT_LIMIT = 40


def _truncate(text: str, limit: int = BUTTON_TEXT_LIMIT) -> str:
    """Безопасное укорачивание надписи кнопки."""
    text = (text or "").strip()
    if len(text) <= limit:
        return text or "—"
    return text[: limit - 1] + "…"


# -------------------------------------
# Главное меню
# -------------------------------------

def main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="📧 Почта", callback_data="mail")
    builder.button(text="🔎 Поиск", callback_data="search")
    builder.adjust(2)
    return builder.as_markup()


# -------------------------------------
# Список непрочитанных писем
# -------------------------------------

def mail_list_keyboard(letters: list[dict]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for letter in letters:
        name = letter.get("sender_name") or letter.get("sender_email") or "Без темы"
        builder.button(
            text=_truncate(name),
            callback_data=f"letter:{letter['uid']}",
        )

    builder.button(text="🏠 В меню", callback_data="main")
    builder.adjust(1)
    return builder.as_markup()


# -------------------------------------
# Карточка письма
# -------------------------------------

def letter_keyboard(uid: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="📄 Текст письма", callback_data=f"text:{uid}")
    builder.button(text="📎 Вложения", callback_data=f"files:{uid}")
    builder.button(text="◀ Назад", callback_data="mail")
    builder.adjust(1)
    return builder.as_markup()


# -------------------------------------
# Кнопки вложений
# -------------------------------------

def files_keyboard(files: list[dict], uid: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for index, file in enumerate(files):
        builder.button(
            text=f"📎 {_truncate(file['filename'])}",
            callback_data=f"file:{uid}:{index}",
        )

    builder.button(text="◀ Назад", callback_data=f"letter:{uid}")
    builder.adjust(1)
    return builder.as_markup()


# -------------------------------------
# Результаты поиска
# -------------------------------------

def search_result_keyboard(letters: list[dict]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for letter in letters:
        builder.button(
            text=f"📌 {_truncate(letter['subject'])}",
            callback_data=f"letter:{letter['uid']}",
        )

    builder.button(text="🏠 В меню", callback_data="main")
    builder.adjust(1)
    return builder.as_markup()
