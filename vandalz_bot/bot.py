import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import Config

from handlers import start, status, log_work

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()

# Регистрация роутеров
dp.include_router(start.router)
dp.include_router(status.router)
dp.include_router(log_work.router)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped.")
