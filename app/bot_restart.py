import asyncio
import os
from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import id_klient
router = Router()

ADMIN_ID = id_klient['bot']

# Глобальные переменные
restart_task = None
countdown_messages = {}


def get_restart_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Restart PC", callback_data="request_restart")
    return keyboard.as_markup()


def get_confirm_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="✅ Подтвердить", callback_data="confirm_restart")
    keyboard.button(text="❌ Отмена", callback_data="cancel_restart")
    return keyboard.as_markup()


async def shutdown_computer():
    await asyncio.sleep(10)
    os.system("shutdown /r /t 1")  # Для Windows
    # Для Linux:
    # os.system("sudo shutdown -r now")


@router.message(F.text == "Рестарт ПК")
async def cmd_restart(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(
            "Бот управления компьютером готов к работе.",
            reply_markup=get_restart_keyboard()
        )
    else:
        await message.answer("У вас нет доступа к этому боту.")


@router.callback_query(F.data == "request_restart")
async def request_restart(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("У вас нет доступа к этой команде.")
        return

    await callback.message.edit_text(
        "Вы уверены, что хотите перезагрузить компьютер?\n"
        "После подтверждения будет 10 секунд на отмену.",
        reply_markup=get_confirm_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == "confirm_restart")
async def confirm_restart(callback: types.CallbackQuery):
    global restart_task, countdown_messages

    if callback.from_user.id != ADMIN_ID:
        await callback.answer("У вас нет доступа к этой команде.")
        return

    restart_task = asyncio.create_task(perform_countdown(callback.message))
    countdown_messages[callback.message.message_id] = True

    await callback.message.edit_text(
        "Компьютер перезагрузится через 10 секунд...",
        reply_markup=get_confirm_keyboard()
    )
    await callback.answer()


async def perform_countdown(message: types.Message):
    global countdown_messages

    for i in range(9, -1, -1):
        if message.message_id not in countdown_messages:
            break

        try:
            await message.edit_text(
                f"Компьютер перезагрузится через {i} секунд...\n"
                "Нажмите ❌ Отмена чтобы прервать.",
                reply_markup=get_confirm_keyboard()
            )
            await asyncio.sleep(1)
        except:
            break

    if message.message_id in countdown_messages:
        await message.edit_text(
            "Перезагрузка компьютера!",
            reply_markup=None
        )
        os.system("shutdown /r /t 1")


@router.callback_query(F.data == "cancel_restart")
async def cancel_restart(callback: types.CallbackQuery):
    global restart_task, countdown_messages

    if callback.from_user.id != ADMIN_ID:
        await callback.answer("У вас нет доступа к этой команде.")
        return

    if callback.message.message_id in countdown_messages:
        del countdown_messages[callback.message.message_id]

    if restart_task and not restart_task.cancelled():
        restart_task.cancel()
        restart_task = None

    await callback.message.edit_text(
        "Перезагрузка отменена!",
        reply_markup=get_restart_keyboard()
    )
    await callback.answer()
