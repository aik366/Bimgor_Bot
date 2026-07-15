import os
import sqlite3
from datetime import datetime
from collections import defaultdict

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from app import keyboards as kb
from app import database as db
from app import run_invest
from config import id_klient
# from fas import *
from app.smart_lab import *
from pochta.gmail_app import *

router = Router()


class Reg(StatesGroup):
    text_1 = State()
    text_2 = State()
    img = State()
    delete_account = State()
    add_surname = State()
    add_account = State()


class Change(StatesGroup):
    change_zakaz = State()
    number_zakaz = State()


class Actions(StatesGroup):
    new_action = State()
    change_action = State()
    edit_action = State()
    add_action = State()
    del_action = State()
    view_action = State()


class PhotoForm(StatesGroup):
    waiting_for_photo = State()  # Шаг 1: Ожидание фото
    waiting_for_caption = State()  # Шаг 2: Ожидание подписи


@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if await db.db_check(message.from_user.id, "Admin"):
        await message.answer("Привет Администратор", reply_markup=kb.kb_admin)


@router.message(F.text == "Объявление")
async def cmd_admin_ad(message: Message, state: FSMContext):
    await state.set_state(Reg.text_1)
    await message.answer("Пишите объявление")


@router.message(Reg.text_1, F.text != '✖ Отмена')
async def reg_admin_text_1(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(msg=message.text)
    full_data = await state.get_data()
    await state.clear()
    if await db.db_check(message.from_user.id, "Admin"):
        for id, name, surname in await db.db_select():
            try:
                await bot.send_message(int(id), f"Привет {name}\n{full_data['msg']}\nАдминистрация!!!")
            except Exception as e:
                await bot.send_message(id_klient['bot'], f'Ошибка при отправке сообщения пользователю {id}: {e}')


@router.message(F.text == "Аккаунты")
async def cmd_admin_ak(message: Message):
    if await db.db_check(message.from_user.id, "Admin"):
        info = ''
        for id, name, surname in await db.db_select():
            info += f"{id}: {name}, {surname}\n"
        await message.answer(info)


# Старт процесса
@router.message(F.text == "Картинка")
async def start_photo_upload(message: Message, state: FSMContext):
    if await db.db_check(message.from_user.id, "Admin"):
        await message.answer("📷 Отправьте фото, к которому нужно добавить подпись")
        await state.set_state(PhotoForm.waiting_for_photo)


# Обработка фото
@router.message(PhotoForm.waiting_for_photo, F.photo)
async def process_photo(message: Message, state: FSMContext):
    # Сохраняем фото
    photo = message.photo[-1]
    await state.update_data(photo_id=photo.file_id)
    # Переходим к ожиданию подписи
    await state.set_state(PhotoForm.waiting_for_caption)
    await message.answer("✅ Фото принято! Теперь введите подпись к фото")


# Обработка подписи
@router.message(PhotoForm.waiting_for_caption, F.text)
async def process_caption(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(caption=message.text)
    full_data = await state.get_data()
    await state.clear()
    for tg_id, name, data in await db.db_select():
        try:
            await bot.send_photo(int(tg_id), full_data['photo_id'],
                                 caption=f"Привет {name}!\n{full_data['caption']}\nАдминистрация!!!")
        except Exception as e:
            await bot.send_message(id_klient['bot'], f'Ошибка при отправке сообщения пользователю {id}: {e}')


@router.message(F.text == "Удалить")
async def cmd_admin_del(message: Message, state: FSMContext):
    await state.set_state(Reg.delete_account)
    await message.answer("Пишите ID аккаунта")


@router.message(Reg.delete_account, F.text != '✖ Отмена')
async def reg_admin_del_account(message: Message, bot: Bot, state: FSMContext):
    if await db.db_check(message.from_user.id, "Admin"):
        await db.db_delete(message.text)
        await bot.send_message(message.from_user.id, "Аккаунт удален")
    await state.clear()


@router.message(F.text == "Добавить")
async def cmd_admin_add(message: Message, state: FSMContext):
    await state.set_state(Reg.add_account)
    await message.answer("Пишите ID аккаунта\nИ через пробел фамилию")


@router.message(Reg.add_account, F.text != '✖ Отмена')
async def reg_admin_add_account(message: Message, bot: Bot, state: FSMContext):
    if await db.db_check(message.from_user.id, "Admin"):
        id_name, name = message.text.split(" ", 1)
        await db.cmd_start_db(id_name, name)
        await bot.send_message(message.from_user.id, "Аккаунт добавлен")
    await state.clear()


@router.message(F.text == "Обновить")
async def cmd_admin_add(message: Message, state: FSMContext):
    await state.set_state(Reg.add_surname)
    await message.answer("Пишите ID аккаунта\nИ через пробел фамилию")


@router.message(Reg.add_surname, F.text != '✖ Отмена')
async def reg_admin_del_surname(message: Message, bot: Bot, state: FSMContext):
    if await db.db_check(message.from_user.id, "Admin"):
        id_name, surname = message.text.split(" ", 1)
        await db.db_update(id_name, surname)
        await bot.send_message(message.from_user.id, "Аккаунт обновлен")
    await state.clear()


@router.message(F.text == "✖ Отмена")
async def cmd_admin_del(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Действие отменено")


@router.message(F.text == "🔙 Назад")
async def cmd_admin_del(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Это Бимгор бот", reply_markup=kb.kb_bot)


@router.message(F.text == "Переписать")
async def cmd_admin_del(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Замена заказа", reply_markup=kb.in_change_order)


@router.message(F.text == "🔄 Рестарт")
async def cmd_restart_bot(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Рестарт через 3 сек", os.startfile("bot_run.vbs"))


@router.callback_query(F.data == "zakaz_value")
async def zakaz_value(call: CallbackQuery):
    if order_number():
        bt = [[(InlineKeyboardButton(text=f"{i}", callback_data=f"bt_{i}")) for i in order_number()]]
        in_kb = InlineKeyboardMarkup(inline_keyboard=bt, row_width=3)
        await call.message.answer(f"Заказ №", reply_markup=in_kb)
    else:
        await call.message.answer(f"Заказов нет!!!")
    await call.answer()


@router.callback_query(F.data.startswith("bt_"))
async def bt_open(call: CallbackQuery, state: FSMContext):
    await state.set_state(Change.number_zakaz)
    call_data = call.data.split("_")[1]
    await state.update_data(num_zakaz=call_data)
    bt_open = [[(InlineKeyboardButton(text=f"Small", callback_data="small_value")),
                (InlineKeyboardButton(text=f"Big", callback_data="big_value")),
                (InlineKeyboardButton(text=f"Delete", callback_data="delete_value"))]]
    in_kb_open = InlineKeyboardMarkup(inline_keyboard=bt_open)
    await call.message.answer(f'Заказ № {call_data}', reply_markup=in_kb_open)
    await call.answer()


@router.callback_query(Change.number_zakaz)
async def smol_value(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == "small_value":
        await call.message.answer("Маленький обновлено!", zamena(1, data['num_zakaz']))
    elif call.data == "big_value":
        await call.message.answer("Большой обновлено!", zamena(0, data['num_zakaz']))
    elif call.data == "delete_value":
        await call.message.answer("Заказ удален!", delete_number(data['num_zakaz']))
    await call.answer()
    await state.clear()


# @router.callback_query(F.data == "open_value")
# async def open_value(call: CallbackQuery):
#     await call.message.answer("Открыта!!!", change_open())
#     await call.answer()


# @router.callback_query(F.data == "close_value")
# async def close_value(call: CallbackQuery):
#     await call.message.answer("Закрыта!!!", change_close())
#     await call.answer()


@router.callback_query(F.data == "change_value")
async def change_value(call: CallbackQuery, state: FSMContext):
    await state.set_state(Change.change_zakaz)
    await call.message.answer(f"Заказов в базе {' '.join(order_number())}\nПишите номер заказа после ???")
    await call.answer()


@router.message(Change.change_zakaz)
async def ms_change_value(message: Message, state: FSMContext):
    number = message.text[3:]
    if message.text.startswith("???"):
        await message.answer(f"Заказ {number} обновлено!!!", change_namber(number))
    else:
        await message.answer("пишите ??? после номер заказа")
    await state.clear()


@router.message(F.text == "Акции")
async def cmd_actions_bot(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выберите действия!!!", reply_markup=kb.in_actions)


@router.callback_query(F.data == "view_actions")
async def view_actions(call: CallbackQuery):
    await call.message.answer(f"{run_invest.main()}", parse_mode="Markdown")
    await call.answer()


def load_portfolio(filepath: str = "DATA/ticker_json.json") -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


@router.callback_query(F.data == "view_add_actions")
async def add_actions(call: CallbackQuery, state: FSMContext):
    portfolio = load_portfolio()
    builder = InlineKeyboardBuilder()
    for ticker, data in portfolio.items():
        if ticker == "IMOEX":
            continue
        builder.button(text=f"{ticker} {data[0]}", callback_data=f"ticker_{ticker}_{data[0]}")
    builder.button(text="Добавить", callback_data="add_actions", style="success")
    builder.adjust(1)
    await call.message.answer(f"Выберите акцию", reply_markup=builder.as_markup())
    await call.answer()


@router.callback_query(F.data.startswith("ticker_"))
async def ticker_open(call: CallbackQuery, state: FSMContext):
    ticker_name, ticker_number = call.data.upper().split("_")[1:]
    await state.update_data(ticker_name=ticker_name, ticker_number=ticker_number)
    builder = InlineKeyboardBuilder()
    builder.button(text="Новое значение", callback_data=f"new_actions")
    builder.button(text="Добавить акции", callback_data=f"change_actions")
    builder.button(text="Удалить", callback_data=f"del_actions")
    builder.button(text="Выход", callback_data="exit_actions", style="danger")
    builder.adjust(1)
    await call.message.answer(f"Выберите действие", reply_markup=builder.as_markup())
    await call.answer()


@router.callback_query(F.data == "new_actions")
async def new_actions(call: CallbackQuery, state: FSMContext):
    await state.set_state(Actions.new_action)
    await call.message.answer("Новое значение акции")
    await call.answer()


@router.message(Actions.new_action)
async def ms_new_action(message: Message, state: FSMContext):
    name_number = int(message.text)
    data = await state.get_data()
    await message.answer(f"Акция {data['ticker_name']} обновлено!!!",
                         update_json_file(data['ticker_name'], name_number), reply_markup=kb.in_actions)
    await state.clear()


@router.callback_query(F.data == "change_actions")
async def change_actions(call: CallbackQuery, state: FSMContext):
    await state.set_state(Actions.change_action)
    await call.message.answer("Количество акций\nКоторую хотите добавить")
    await call.answer()


@router.message(Actions.change_action)
async def ms_change_action(message: Message, state: FSMContext):
    number = int(message.text)
    data = await state.get_data()
    number += int(data['ticker_number'])
    await message.answer(f"Акция {data['ticker_name']} обновлено!!!", update_json_file(data['ticker_name'], number),
                         reply_markup=kb.in_actions)
    await state.clear()


@router.callback_query(F.data == "del_actions")
async def del_actions(call: CallbackQuery, state: FSMContext):
    del_keyboard = InlineKeyboardBuilder()
    del_keyboard.button(text="Удалить", callback_data=f"delete_actions")
    del_keyboard.button(text="Выход", callback_data="exit_actions", style="danger")
    del_keyboard.adjust(2)
    data = await state.get_data()
    await call.message.answer(f"Удалить акцию {data['ticker_name']}?", reply_markup=del_keyboard.as_markup())
    await call.answer()


@router.callback_query(F.data == "delete_actions")
async def delete_actions(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.answer(f"Акция {data['ticker_name']} удалена!!!", delete_json_file(data['ticker_name']))
    await state.clear()
    await call.answer()


@router.callback_query(F.data == "exit_actions")
async def exit_actions(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите действия!!!", reply_markup=kb.in_actions)
    await state.clear()
    await call.answer()


@router.callback_query(F.data == "add_actions")
async def add_actions(call: CallbackQuery, state: FSMContext):
    await state.set_state(Actions.add_action)
    await call.message.answer("Имя акции пробел\nколичество акций\nНапример: LKOH 100")
    await call.answer()


@router.message(Actions.add_action)
async def ms_add_action(message: Message, state: FSMContext):
    name_number = message.text.upper().split(" ")
    await message.answer(f"Акция {name_number[0]} добавлена!!!", update_json_file(name_number[0], name_number[1]),
                         reply_markup=kb.in_actions)
    await state.clear()


# ================= НАСТРОЙКИ =================
DB_NAME = "DATA/finance.db"

# Словарь для вывода месяцев на русском
MONTHS_RU = {
    1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель",
    5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
    9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"
}


# =============================================

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Машина состояний (FSM)
class AddState(StatesGroup):
    waiting_for_amount = State()


class EditState(StatesGroup):
    waiting_for_amount = State()
    waiting_for_date = State()


# ================= ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =================
def format_date_for_user(db_date: str) -> str:
    """Преобразует дату из БД (YYYY-MM-DD) в формат для пользователя (DD.MM.YYYY)"""
    y, m, d = db_date.split("-")
    return f"{d}.{m}.{y}"


async def show_edit_list(target):
    """Показывает список записей для редактирования"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount, date FROM records ORDER BY date ASC")
    rows = cursor.fetchall()
    conn.close()

    builder = InlineKeyboardBuilder()
    if rows:
        for row in rows:
            r_id, amount, date = row
            amount_str = f"{amount:g}"
            # ИЗМЕНЕНИЕ: Форматируем дату для кнопки
            user_date = format_date_for_user(date)
            builder.row(InlineKeyboardButton(text=f"{amount_str} ₽ | {user_date}", callback_data=f"edit_rec:{r_id}"))

    builder.row(InlineKeyboardButton(text="« В главное меню", callback_data="back_to_start"))

    text = "Выберите запись для редактирования:" if rows else "📭 Нет записей для редактирования."

    if isinstance(target, Message):
        await target.answer(text, reply_markup=builder.as_markup())
    elif isinstance(target, CallbackQuery):
        await target.message.edit_text(text, reply_markup=builder.as_markup())
        await target.answer()


# ================= ОБРАБОТЧИКИ =================

@router.callback_query(F.data == "view_add_finance")
async def view_finance(call: CallbackQuery, state: FSMContext):
    init_db()
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➕ Добавить", callback_data="action_add"))
    builder.row(InlineKeyboardButton(text="📊 Просмотр", callback_data="action_view"))
    builder.row(InlineKeyboardButton(text="✏️ Редактировать", callback_data="action_edit"))
    await call.message.answer("👋 Добро пожаловать! Выберите действие:", reply_markup=builder.as_markup())
    await state.clear()
    await call.answer()


@router.callback_query(F.data == "back_to_start")
async def cb_back_to_start(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➕ Добавить", callback_data="action_add"))
    builder.row(InlineKeyboardButton(text="📊 Просмотр", callback_data="action_view"))
    builder.row(InlineKeyboardButton(text="✏️ Редактировать", callback_data="action_edit"))
    await callback.message.edit_text("Выберите действие:", reply_markup=builder.as_markup())
    await callback.answer()


# --- ДОБАВИТЬ ---
@router.callback_query(F.data == "action_add")
async def cb_add(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AddState.waiting_for_amount)
    await callback.message.edit_text("💰 Введите сумму для добавления:")
    await callback.answer()


@router.message(AddState.waiting_for_amount)
async def msg_add_amount(message: Message, state: FSMContext):
    try:
        amount = float(message.text.replace(',', '.'))

        # Для БД сохраняем YYYY-MM-DD (для сортировки)
        db_date = datetime.now().strftime("%Y-%m-%d")
        # Для сообщения пользователю используем DD.MM.YYYY
        user_date = datetime.now().strftime("%d.%m.%Y")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO records (amount, date) VALUES (?, ?)", (amount, db_date))
        conn.commit()
        conn.close()

        # ИЗМЕНЕНИЕ: Выводим дату в формате ДД.ММ.ГГГГ
        await message.answer(f"✅ Сохранено: **{amount:g} ₽** на {user_date}", parse_mode="Markdown")
        await state.clear()
        # await view_finance(message, state)
    except ValueError:
        await message.answer("❌ Пожалуйста, введите корректное число (например, 1500 или 1500.50).")


# --- ПРОСМОТР ---
@router.callback_query(F.data == "action_view")
async def cb_view(callback: CallbackQuery):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT amount, date FROM records ORDER BY date ASC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        await callback.message.edit_text("📭 Записей пока нет.")
        await callback.answer()
        return

    months = defaultdict(list)
    grand_total = 0.0

    for amount, date in rows:
        month = date[:7]  # Формат YYYY-MM
        months[month].append((amount, date))
        grand_total += amount

    text = "📊 **Статистика по месяцам:**\n\n"

    for month, records in sorted(months.items()):
        month_total = sum(record[0] for record in records)

        year, month_num = month.split("-")
        month_name = f"{MONTHS_RU[int(month_num)]} {year}"

        text += f"📅 **{month_name}**\n"
        for amt, full_date in records:
            # Преобразуем дату из YYYY-MM-DD в DD.MM.YYYY
            user_date = format_date_for_user(full_date)
            text += f"  • {amt:g} ₽ - {user_date}\n"
        text += f"  _Итого за месяц: {month_total:g} ₽_\n\n"

    text += f"💰 **Общая сумма: {grand_total:g} ₽**"

    if len(text) > 4000:
        text = text[:3900] + "\n\n⚠️ _Список слишком длинный и был обрезан._"

    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.answer()


# --- РЕДАКТИРОВАТЬ (Список) ---
@router.callback_query(F.data == "action_edit")
async def cb_edit(callback: CallbackQuery):
    await show_edit_list(callback)


# --- РЕДАКТИРОВАТЬ (Выбор конкретной записи) ---
@router.callback_query(F.data.startswith("edit_rec:"))
async def cb_edit_rec(callback: CallbackQuery):
    record_id = int(callback.data.split(":")[1])
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="💰 Изменить сумму", callback_data=f"edit_amt:{record_id}"))
    builder.row(InlineKeyboardButton(text="📅 Изменить дату", callback_data=f"edit_dt:{record_id}"))
    builder.row(InlineKeyboardButton(text="🗑 Удалить запись", callback_data=f"del_rec:{record_id}"))
    builder.row(InlineKeyboardButton(text="« Назад к списку", callback_data="action_edit"))

    await callback.message.edit_text(f"⚙️ Запись #{record_id}. Выберите действие:", reply_markup=builder.as_markup())
    await callback.answer()


# --- Изменение суммы ---
@router.callback_query(F.data.startswith("edit_amt:"))
async def cb_edit_amt(callback: CallbackQuery, state: FSMContext):
    record_id = int(callback.data.split(":")[1])
    await state.update_data(record_id=record_id)
    await state.set_state(EditState.waiting_for_amount)
    await callback.message.edit_text("💰 Введите новую сумму:")
    await callback.answer()


@router.message(EditState.waiting_for_amount)
async def msg_edit_amt(message: Message, state: FSMContext):
    try:
        new_amount = float(message.text.replace(',', '.'))
        data = await state.get_data()
        record_id = data.get("record_id")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE records SET amount = ? WHERE id = ?", (new_amount, record_id))
        conn.commit()
        conn.close()

        await message.answer(f"✅ Сумма успешно обновлена на **{new_amount:g} ₽**", parse_mode="Markdown")
        await state.clear()
        await show_edit_list(message)
    except ValueError:
        await message.answer("❌ Пожалуйста, введите корректное число.")


# --- Изменение даты (ОБНОВЛЕНО) ---
@router.callback_query(F.data.startswith("edit_dt:"))
async def cb_edit_dt(callback: CallbackQuery, state: FSMContext):
    record_id = int(callback.data.split(":")[1])
    await state.update_data(record_id=record_id)
    await state.set_state(EditState.waiting_for_date)
    # ИЗМЕНЕНИЕ: Просим формат ДД.ММ.ГГГГ
    await callback.message.edit_text("📅 Введите новую дату в формате **ДД.ММ.ГГГГ** (например, 15.01.2026):",
                                     parse_mode="Markdown")
    await callback.answer()


@router.message(EditState.waiting_for_date)
async def msg_edit_dt(message: Message, state: FSMContext):
    new_date_input = message.text.strip()
    try:
        # 1. Проверяем, что пользователь ввел дату в формате ДД.ММ.ГГГГ
        parsed_date = datetime.strptime(new_date_input, "%d.%m.%Y")
        # 2. Конвертируем её в формат ГГГГ-ММ-ДД для корректного сохранения и сортировки в БД
        db_date = parsed_date.strftime("%Y-%m-%d")
    except ValueError:
        await message.answer("❌ Неверный формат даты. Используйте строго **ДД.ММ.ГГГГ** (например, 15.01.2026).")
        return

    data = await state.get_data()
    record_id = data.get("record_id")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Сохраняем в БД в формате ГГГГ-ММ-ДД
    cursor.execute("UPDATE records SET date = ? WHERE id = ?", (db_date, record_id))
    conn.commit()
    conn.close()

    # Пользователю показываем в привычном формате
    await message.answer(f"✅ Дата успешно обновлена на **{new_date_input}**", parse_mode="Markdown")
    await state.clear()
    await show_edit_list(message)


# --- Удаление записи ---
@router.callback_query(F.data.startswith("del_rec:"))
async def cb_del_rec(callback: CallbackQuery):
    record_id = int(callback.data.split(":")[1])

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()

    await callback.answer("✅ Запись удалена")
    await show_edit_list(callback)