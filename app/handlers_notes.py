from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.text_decorations import html_decoration
import app.database as db
import app.keyboards_notes as kb
from app.keyboards import kb_bot

router_notes = Router()


class Notes(StatesGroup):
    fsm_note_name = State()
    fsm_note_text = State()
    note_number = State()
    note_list = State()
    note_all = State()
    note_delete = State()
    note_edit = State()
    name_text = State()
    note_new_add = State()
    new_text = State()
    add_text = State()


# Словарь эмодзи для типов заметок
type_dict = {
    'text': '📝',
    'photo': '🖼️',
    'document': '📄',
    'voice': '🎤',
    'audio': '🎵',
    'video': '📽️',
    'video_note': '🎦'
}


# --- НОВАЯ ФУНКЦИЯ: Преобразует форматирование Telegram в HTML ---
def get_html_text(text: str, entities: list = None) -> str:
    if not entities:
        return html_decoration.quote(text)

    # Сортируем сущности, чтобы обрабатывать их последовательно
    sorted_entities = sorted(entities, key=lambda e: e.offset)

    result = ""
    last_offset = 0

    for entity in sorted_entities:
        # Добавляем текст до текущей сущности
        result += html_decoration.quote(text[last_offset:entity.offset])

        # Получаем текст сущности
        entity_text = text[entity.offset:entity.offset + entity.length]
        entity_text_quoted = html_decoration.quote(entity_text)

        # Оборачиваем в HTML теги в зависимости от типа
        if entity.type == 'bold':
            result += f"<b>{entity_text_quoted}</b>"
        elif entity.type == 'italic':
            result += f"<i>{entity_text_quoted}</i>"
        elif entity.type == 'underline':
            result += f"<u>{entity_text_quoted}</u>"
        elif entity.type == 'strikethrough':
            result += f"<s>{entity_text_quoted}</s>"
        elif entity.type == 'code':
            result += f"<code>{entity_text_quoted}</code>"
        elif entity.type == 'pre':
            result += f"<pre>{entity_text_quoted}</pre>"
        elif entity.type == 'blockquote':
            result += f"<blockquote>{entity_text_quoted}</blockquote>"
        elif entity.type == 'text_link':
            url = entity.url
            result += f"<a href='{url}'>{entity_text_quoted}</a>"
        else:
            result += entity_text_quoted

        last_offset = entity.offset + entity.length

    # Добавляем оставшийся текст
    result += html_decoration.quote(text[last_offset:])

    return result


@router_notes.message(F.text == '📝Заметки')
async def note_text(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Это меню заметок", reply_markup=kb.note_list)


@router_notes.message(F.text == '📝Добавить заметку')
async def note_text_name(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Notes.fsm_note_name)
    await message.answer("Пишите название заметки 👇", reply_markup=kb.note_list)


@router_notes.message(Notes.fsm_note_name)
async def text_note(message: Message, state: FSMContext):
    # Название сохраняем как есть (или тоже можно форматировать)
    await state.update_data(fsm_note_name=message.text)
    await state.set_state(Notes.fsm_note_text)
    await message.answer(
        "Теперь отправьте содержимое заметки:\n\n"
        "📝 Текст - для текстовой заметки\n"
        "📷 Фото - для фото заметки\n"
        "🎤 Аудио/голосовое - для аудио заметки\n"
        "🎬 Видео - для видео заметки 👇",
        reply_markup=kb.note_list,
        parse_mode='HTML'
    )


@router_notes.message(Notes.fsm_note_text)
async def save_note(message: Message, state: FSMContext):
    file_id, note_type = None, None

    if message.content_type == 'text':
        # ✅ ИСПОЛЬЗУЕМ ФУНКЦИЮ ДЛЯ СОХРАНЕНИЯ ФОРМАТИРОВАНИЯ
        html_text = get_html_text(message.text, message.entities)
        await state.update_data(fsm_note_text=html_text)
        data_state = await state.get_data()
        await db.add_note(
            message.from_user.id,
            data_state['fsm_note_name'],
            data_state['fsm_note_text'],
            note_type='text'
        )
        await state.clear()
        return await message.answer("Заметка сохранена", reply_markup=kb.note_list)

    if message.content_type == 'photo':
        file_id = message.photo[-1].file_id
        note_type = 'photo'
    elif message.content_type == 'document':
        file_id = message.document.file_id
        note_type = 'document'
    elif message.content_type == 'voice':
        file_id = message.voice.file_id
        note_type = 'voice'
    elif message.content_type == 'audio':
        file_id = message.audio.file_id
        note_type = 'audio'
    elif message.content_type == 'video':
        file_id = message.video.file_id
        note_type = 'video'
    elif message.content_type == 'video_note':
        file_id = message.video_note.file_id
        note_type = 'video_note'

    # Для медиа тоже сохраняем форматирование подписи
    caption_text = '----'
    if message.caption:
        caption_text = get_html_text(message.caption, message.caption_entities)

    await state.update_data(fsm_note_text=caption_text)
    data_state = await state.get_data()
    await db.add_note(
        message.from_user.id,
        data_state['fsm_note_name'],
        data_state['fsm_note_text'],
        note_type=note_type,
        file_id=file_id
    )
    await message.answer("Заметка сохранена", reply_markup=kb.note_list)
    await state.clear()


@router_notes.message(F.text == '📋Мои заметки')
async def my_note_text(message: Message, state: FSMContext):
    await state.clear()
    notes_dict = await db.select_note(message.from_user.id)

    if notes_dict:
        await state.update_data(note_list=notes_dict)
        in_kb = []
        for key in notes_dict:
            in_kb.append([InlineKeyboardButton(
                text=f'{type_dict[notes_dict[key][2]]}{notes_dict[key][0]}',
                callback_data=f'notes_{key}'
            )])
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=in_kb,
            resize_keyboard=True,
            one_time_keyboard=True
        )
        await message.answer("Ваши заметки", reply_markup=keyboard)
    else:
        await message.answer("У вас нет заметок", reply_markup=kb.note_list)


@router_notes.callback_query(F.data.startswith('notes_'))
async def note_view(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_namber=call.data.split('_')[1])
    await state.set_state(Notes.note_all)

    data_state = await state.get_data()
    num = int(data_state['note_namber'])
    note_data = data_state['note_list'][num]

    note_type = note_data[2]
    file_id = note_data[3]
    caption = note_data[1]

    try:
        if note_type == 'photo':
            await call.message.answer_photo(
                photo=file_id,
                caption=caption,
                parse_mode='HTML',  # ✅ Включено
                reply_markup=kb.edit_note
            )
        elif note_type == 'document':
            await call.message.answer_document(
                document=file_id,
                caption=caption,
                parse_mode='HTML',  # ✅ Включено
                reply_markup=kb.edit_note
            )
        elif note_type == 'voice':
            await call.message.answer_voice(
                voice=file_id,
                caption=caption,
                parse_mode='HTML',  # ✅ Включено
                reply_markup=kb.edit_note
            )
        elif note_type == 'audio':
            await call.message.answer_audio(
                audio=file_id,
                caption=caption,
                parse_mode='HTML',  # ✅ Включено
                reply_markup=kb.edit_note
            )
        elif note_type == 'video':
            await call.message.answer_video(
                video=file_id,
                caption=caption,
                parse_mode='HTML',  # ✅ Включено
                reply_markup=kb.edit_note
            )
        elif note_type == 'video_note':
            # Видео-кружочки не поддерживают caption
            await call.message.answer_video_note(
                video_note=file_id,
                reply_markup=kb.edit_note
            )
        elif note_type == 'text':
            await call.message.edit_text(
                text=caption,
                parse_mode='HTML',  # ✅ Включено
                reply_markup=kb.edit_note
            )
        else:
            await call.message.answer(
                text=f"⚠️ Неизвестный тип заметки: {note_type}\nСодержимое: {caption}",
                reply_markup=kb.edit_note
            )
    except Exception as e:
        await call.message.answer(
            text=f"⚠️ Ошибка доступа к файлу!\n\nНазвание: {note_data[0]}\nТекст: {caption}",
            reply_markup=kb.edit_note
        )
        print(f"Error sending note: {e}")

    await call.answer()


@router_notes.callback_query(Notes.note_all, F.data == 'note_edit')
async def edit_note(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_all=call.data)
    await state.set_state(Notes.note_edit)
    await call.message.answer("Имя заметки или текст заметки?", reply_markup=kb.note_edit)
    await call.answer()


@router_notes.callback_query(Notes.note_edit, F.data == 'edit_name')
async def edit_note_name(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_edit=call.data)
    await state.set_state(Notes.name_text)
    await call.message.answer("Пишите Имя заметки 👇", reply_markup=kb.note_list)
    await call.answer()


@router_notes.message(Notes.name_text)
async def save_note_name(message: Message, state: FSMContext):
    await state.update_data(name_text=message.text)
    data_state = await state.get_data()
    num = int(data_state['note_namber'])
    note_name = data_state['note_list'][num][0]
    note_text = data_state['note_list'][num][1]
    await db.update_note_name(message.from_user.id, data_state['name_text'], note_name, note_text)
    await message.answer("Имя заметки сохранено", reply_markup=kb.note_list)
    await state.clear()


@router_notes.callback_query(Notes.note_edit, F.data == 'edit_text')
async def edit_note_text(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_edit=call.data)
    await state.set_state(Notes.note_new_add)
    await call.message.answer("Добавить к тексту или новый текст?", reply_markup=kb.note_edit_content)
    await call.answer()


@router_notes.callback_query(Notes.note_new_add, F.data == 'new_text')
async def note_new(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_edit_text=call.data)
    await state.set_state(Notes.new_text)
    await call.message.answer("Пишите новый текст заметки 👇", reply_markup=kb.note_list)
    await call.answer()


@router_notes.message(Notes.new_text)
async def note_new_text(message: Message, state: FSMContext):
    # ✅ Сохраняем форматирование при редактировании
    html_text = get_html_text(message.text, message.entities)
    await state.update_data(new_text=html_text)
    data_state = await state.get_data()
    num = int(data_state['note_namber'])
    note_name = data_state['note_list'][num][0]
    note_text = data_state['note_list'][num][1]
    await db.update_note_text(message.from_user.id, data_state['new_text'], note_name, note_text)
    await message.answer("Новый текст сохранён", reply_markup=kb.note_list)
    await state.clear()


@router_notes.callback_query(Notes.note_new_add, F.data == 'add_text')
async def note_add(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_edit_text=call.data)
    await state.set_state(Notes.add_text)
    await call.message.answer("Пишите текст для добавления к заметке 👇", reply_markup=kb.note_list)
    await call.answer()


@router_notes.message(Notes.add_text)
async def note_add_text(message: Message, state: FSMContext):
    # ✅ Сохраняем форматирование при добавлении
    html_text = get_html_text(message.text, message.entities)
    await state.update_data(add_text=html_text)
    data_state = await state.get_data()
    num = int(data_state['note_namber'])
    note_name = data_state['note_list'][num][0]
    note_text = data_state['note_list'][num][1]

    if note_text == '----':
        all_text = f"{data_state['add_text']}"
    else:
        all_text = f"{note_text}\n----\n{data_state['add_text']}"

    await db.update_note_text(message.from_user.id, all_text, note_name, note_text)
    await message.answer("Текст добавлен к заметке", reply_markup=kb.note_list)
    await state.clear()


@router_notes.callback_query(Notes.note_all, F.data == 'note_delete')
async def delete_note(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_all=call.data)
    await state.set_state(Notes.note_delete)
    data_state = await state.get_data()
    num = int(data_state['note_namber'])
    await call.message.answer(
        f"{type_dict[data_state['note_list'][num][2]]}{data_state['note_list'][num][0]}",
        reply_markup=kb.note_delete
    )
    await call.answer()


@router_notes.callback_query(Notes.note_delete, F.data == 'delete_note')
async def delete_note_es(call: CallbackQuery, state: FSMContext):
    await state.update_data(note_delete=call.data)
    data_state = await state.get_data()
    num = int(data_state['note_namber'])
    await db.note_delete(
        call.from_user.id,
        data_state['note_list'][num][0],
        data_state['note_list'][num][1]
    )
    await call.message.answer("Заметка удалена!!!", reply_markup=kb.note_list)
    await call.answer()
    await state.clear()


@router_notes.callback_query(F.data == 'cancel')
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Действие отменено", reply_markup=kb.add_user_data)
    await state.clear()
    await call.answer()


@router_notes.callback_query(F.data == 'cancel_note')
async def cancel_note(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Действие отменено", reply_markup=kb.note_list)
    await state.clear()
    await call.answer()


@router_notes.message(F.text == '🏠Главное меню')
async def start_note_menu(message: Message, state: FSMContext):
    await message.answer('Главное меню', reply_markup=kb_bot)
    await state.clear()
