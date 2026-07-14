from aiogram import F, Router

from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from app.keyboards import kb_frezer, kb_frezer_it
from app.it_stanok import value_freza, value_tolshina

router = Router()


class Reg(StatesGroup):
    it_order = State()
    it_freza = State()
    it_visota = State()
    it_order_tolshina = State()
    it_select_tolshina = State()
    it_volue_tolshina = State()


@router.message(F.text == "it_станок")
async def number_order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Это it станок", reply_markup=kb_frezer_it)


@router.message(F.text == "↩️ Назад")
async def number_order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Начало", reply_markup=kb_frezer)


@router.message(F.text == "№ фрезы")
async def number_order(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Reg.it_order)
    await message.answer("Введите номер заказа: ")


@router.message(F.text == "Толщина МДФ")
async def number_order_tolshina(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Reg.it_order_tolshina)
    await message.answer("Введите номер заказа: ")


@router.message(Reg.it_order_tolshina)
async def volue_tolshina(message: Message, state: FSMContext):
    await state.update_data(n_order=message.text + "it")
    tolshina = [[InlineKeyboardButton(text="16 МДФ", callback_data="mdf_16"),
                 InlineKeyboardButton(text="19 МДФ", callback_data="mdf_19"),
                 InlineKeyboardButton(text="22 МДФ", callback_data="mdf_22")]]
    await message.answer("Выберите МДФ: ", reply_markup=InlineKeyboardMarkup(inline_keyboard=tolshina))


@router.callback_query(F.data.startswith("mdf_"))
async def mdf_tolshina(call: CallbackQuery, state: FSMContext):
    if call.data == "mdf_16":
        await state.update_data(select=call.data)
    elif call.data == "mdf_19":
        await state.update_data(select=call.data)
    elif call.data == "mdf_22":
        await state.update_data(select=call.data)
    else:
        await call.message.answer("Ошибка")
        await state.clear()
    await state.set_state(Reg.it_volue_tolshina)
    await call.message.answer("Введите значение толщины: ")
    await call.answer()


@router.message(Reg.it_volue_tolshina)
async def itogo_tolshina(message: Message, state: FSMContext):
    await state.update_data(n_visota=message.text)
    data = await state.get_data()
    await message.answer(value_tolshina(data['n_order'][:-2], int(data['select'][-2:]), data['n_visota']))
    await state.clear()


@router.message(Reg.it_order)
async def number_freza(message: Message, state: FSMContext):
    await state.update_data(n_order=message.text + "it")
    await state.set_state(Reg.it_freza)
    await message.answer("Введите номер фрезы: ")


@router.message(Reg.it_freza)
async def visota_freza(message: Message, state: FSMContext):
    await state.update_data(n_freza=message.text)
    await state.set_state(Reg.it_visota)
    await message.answer("Введите значение фрезы: ")


@router.message(Reg.it_visota)
async def itogo_freza(message: Message, state: FSMContext):
    await state.update_data(n_visota=message.text.replace(",", "."))
    data = await state.get_data()
    await message.answer(value_freza(data['n_order'][:-2], data['n_freza'], data['n_visota']))
    await state.clear()


@router.callback_query(F.data == "сancel_standok")
async def cancel(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer("Действие отменено", reply_markup=kb_frezer)
    await call.answer()
