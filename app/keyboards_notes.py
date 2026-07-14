from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)


edit_note = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✏️Редактировать', callback_data='note_edit', style='success'),
     InlineKeyboardButton(text='🗑️Удалить', callback_data='note_delete', style='danger')],
], resize_keyboard=True)

# Подтверждение удаления
delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🗑️Удалить', callback_data='delete'),
     InlineKeyboardButton(text='❌Отмена', callback_data='cancel')],
], resize_keyboard=True)

# Подтверждение удаления заметки
note_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🗑️Удалить', callback_data='delete_note'),
     InlineKeyboardButton(text='❌Отмена', callback_data='cancel_note')],
], resize_keyboard=True)

# Выбор что редактировать в заметке (Имя или Текст)
note_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Имя заметки', callback_data='edit_name'),
     InlineKeyboardButton(text='Текст заметки', callback_data='edit_text')],
], resize_keyboard=True)

# Выбор режима редактирования текста (Добавить или Новый)
note_edit_content = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить', callback_data='add_text'),
     InlineKeyboardButton(text='Новый', callback_data='new_text')],
], resize_keyboard=True)

# Кнопка отмены
cancel_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❌Отмена', callback_data='cancel')],
], resize_keyboard=True)


# Меню внутри раздела Заметки
note_list = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📝Добавить заметку"), KeyboardButton(text="📋Мои заметки")],
    [KeyboardButton(text="🏠Главное меню"), KeyboardButton(text="❌Отмена")]
], resize_keyboard=True)
