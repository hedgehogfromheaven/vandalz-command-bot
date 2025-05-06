from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
import asyncio

from config import settings
from handlers import start, status, log_work

async def main():
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        start.router,
        status.router,
        log_work.router
    )

    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="status", description="Check car status"),
        BotCommand(command="log_work", description="Log new work")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())