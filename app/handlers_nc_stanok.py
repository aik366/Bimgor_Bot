from aiogram import Bot, F, Router

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from app.nc_stanok import podkladka, speed_change, add_nc_freza
from app.ss_stanok import add_ss_freza
from app.it_stanok import add_it_freza

from app.keyboards import kb_frezer, kb_frezer_nc

router = Router()


class Reg(StatesGroup):
    n_order = State()
    podklad = State()
    num_order = State()
    num_freza = State()
    speed_freza = State()
    order_num = State()
    stanok = State()


@router.message(F.text == "nc_станок")
async def number_order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Это nc станок", reply_markup=kb_frezer_nc)


@router.message(F.text == "↩️ Назад")
async def number_order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Начало", reply_markup=kb_frezer)


@router.message(F.text == "Подклад")
async def number_order(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Reg.n_order)
    await message.answer("Введите номер заказа: ")


@router.message(Reg.n_order)
async def tol_podkladki(message: Message, state: FSMContext):
    await state.update_data(n_order=message.text + "nc")
    await state.set_state(Reg.podklad)
    await message.answer("Введите толщину подкладки: ")


@router.message(Reg.podklad)
async def podklad(message: Message, state: FSMContext):
    await state.update_data(podklad=message.text)
    data = await state.get_data()
    await message.answer(f"{podkladka(data['n_order'], data['podklad'])}")
    await state.clear()


@router.message(F.text == "Подача")
async def num_order(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Reg.num_order)
    await message.answer("Введите номер заказа: ")


@router.message(Reg.num_order)
async def num_freza(message: Message, state: FSMContext):
    await state.update_data(num_order=message.text + "nc")
    await state.set_state(Reg.num_freza)
    await message.answer("Введите номер фрезы: ")


@router.message(Reg.num_freza)
async def speed_podachi(message: Message, state: FSMContext):
    await state.update_data(num_freza=message.text)
    await state.set_state(Reg.speed_freza)
    await message.answer("Введите скорость подачи: ")


@router.message(Reg.speed_freza)
async def podacha(message: Message, state: FSMContext):
    await state.update_data(speed_freza=message.text)
    data = await state.get_data()
    await message.answer(f"{speed_change(data['num_order'], data['num_freza'], data['speed_freza'])}")
    await state.clear()


@router.message(F.text == "+132 фреза")
async def order_num(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Reg.order_num)
    await message.answer("Введите номер заказа: ")


@router.message(Reg.order_num)
async def stanok(message: Message, state: FSMContext):
    await state.update_data(order_num=message.text)
    await state.set_state(Reg.stanok)
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ss", callback_data="ss_stanok"),
         InlineKeyboardButton(text="nc", callback_data="nc_stanok"),
         InlineKeyboardButton(text="it", callback_data="it_stanok")],
        [InlineKeyboardButton(text="✖отмена", callback_data="сancel_standok")]])
    await message.answer("Выберите станок: ", reply_markup=inline_kb)


@router.callback_query(Reg.stanok, F.data[-6:] == "stanok")
async def arkhive_order(call: CallbackQuery, state: FSMContext):
    await state.update_data(stanok=call.data[:2])
    data = await state.get_data()
    await call.message.answer(f"Номер заказа: {data['order_num']}\nСтанок: {data['stanok']}_станок",
                              reply_markup=kb_frezer)
    if data['stanok'] == "ss":
        await call.message.answer(f"{add_ss_freza(data['order_num'])}")
    elif data['stanok'] == "nc":
        await call.message.answer(f"{add_nc_freza(data['order_num'])}")
    elif data['stanok'] == "it":
        await call.message.answer(f"{add_it_freza(data['order_num'])}")
    await state.clear()
    await call.answer()


@router.callback_query(F.data == "сancel_standok")
async def cancel(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer("Действие отменено", reply_markup=kb_frezer)
    await call.answer()
