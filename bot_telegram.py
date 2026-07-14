import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from config import TOKEN, id_klient
from app import handlers, handlers_bimgor, handlers_admin, handlers_nc_stanok, handlers_it_stanok, archive, bot_restart, \
    handlers_email
from fas import send_msg_cron, shutdown, update_func, taskkill, zamen_smol, zamen_big
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import BotCommand, BotCommandScopeDefault
from app.handlers_notes import router_notes

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='info', description='Информация'),
                BotCommand(command='admin', description='Администратор'), ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot():
    await set_commands()
    await bot.send_message(id_klient['bot'], f'Я запущен🥳.')


async def stop_bot():
    await bot.send_message(id_klient['bot'], 'Бот остановлен. За что?😔')


async def main():
    dp.include_routers(handlers_admin.router, handlers.router, handlers_nc_stanok.router, handlers_it_stanok.router,
                       archive.router, bot_restart.router, router_notes, handlers_email.router, handlers_bimgor.router)
    # регистрация функций
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_msg_cron, 'cron', day_of_week='mon-fri', hour=17, minute=00,
                      start_date=datetime.now(), args=(dp,))
    # scheduler.add_job(shutdown, 'cron', day_of_week='mon-sun', hour=5, minute=30,
    #                   start_date=datetime.now(), args=(dp,))
    scheduler.add_job(update_func, 'interval', minutes=15, args=(dp,))
    scheduler.add_job(taskkill, 'interval', minutes=30, args=(dp,))

    # scheduler.add_job(zamen_smol, 'cron', day_of_week='mon-fri', hour=16, minute=50,
    #                   start_date=datetime.now(), args=(dp,))
    # scheduler.add_job(zamen_big, 'cron', day_of_week='mon-fri', hour=17, minute=10,
    #                   start_date=datetime.now(), args=(dp,))

    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    try:
        print('Бот запущен!!!')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
