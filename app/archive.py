from aiogram import Bot, F, Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from config import put_old, put_555ss, put_555nc, put_555it
from time import strftime
import shutil
import os

router = Router()

year, year_1, year_2 = strftime('%Y'), str(int(strftime('%Y')) - 1), str(int(strftime('%Y')) - 2)


def copy_archive(year, stanok, zakaz):
    for folder in os.listdir(f"{put_old}{year}/"):
        if int(zakaz[:4]) < int(folder.split('_')[-1]):
            puth = f"{put_old}{year}/{folder}/{stanok}/{zakaz}"
            if os.path.exists(puth):
                if zakaz[4:] == 'h':
                    shutil.copytree(puth, f"{put_555ss}/{zakaz}")
                elif zakaz[4:] == 'nc':
                    shutil.copytree(puth, f"{put_555nc}/{zakaz}")
                elif zakaz[4:] == 'it':
                    shutil.copytree(puth, f"{put_555it}/{zakaz}")
                return 'Копирование завершено.'
            else:
                return 'нет такого заказа.'


class Reg(StatesGroup):
    a_year = State()
    a_stanok = State()
    zakaz_n = State()


@router.message(F.text == "Архив")
async def arkhive_year(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Reg.a_year)
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{year_2}", callback_data=f"yr_{year_2}"),
         InlineKeyboardButton(text=f"{year_1}", callback_data=f"yr_{year_1}"),
         InlineKeyboardButton(text=f"{year}", callback_data=f"yr_{year}")]])
    await message.answer("Выберите год:", reply_markup=inline_kb)


@router.callback_query(Reg.a_year, F.data[:2] == "yr")
async def arkhive_stanok(call: CallbackQuery, state: FSMContext):
    await state.update_data(a_year=call.data[3:])
    await state.set_state(Reg.a_stanok)
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ss", callback_data="st_ss"),
         InlineKeyboardButton(text="nc", callback_data="st_nc"),
         InlineKeyboardButton(text="it", callback_data="st_it")]])
    await call.message.answer("Выберите станок: ", reply_markup=inline_kb)
    await call.answer()


@router.callback_query(Reg.a_stanok, F.data[:2] == "st")
async def arkhive_order(call: CallbackQuery, state: FSMContext):
    await state.update_data(a_stanok=call.data[3:])
    await state.set_state(Reg.zakaz_n)
    data = await state.get_data()
    await call.message.answer(f"год: {data['a_year']} станок: {data['a_stanok']}\nВведите номер заказа: ")
    await call.answer()


@router.message(Reg.zakaz_n)
async def arkhive_all(message: Message, state: FSMContext):
    data, message_text = await state.get_data(), ''
    if data["a_stanok"] == 'ss':
        message_text = message.text + 'h'
    elif data["a_stanok"] == 'nc':
        message_text = message.text + 'nc'
    elif data["a_stanok"] == 'it':
        message_text = message.text + 'it'
    await state.update_data(zakaz_n=message_text)
    data = await state.get_data()
    await message.answer(copy_archive(data['a_year'], data['a_stanok'], data['zakaz_n']))
    await state.clear()


if __name__ == "__main__":
    pass
