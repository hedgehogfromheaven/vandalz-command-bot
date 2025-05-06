from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import Router
import asyncio
import logging
import os

from handlers import start, status, log_work

# Настройка логгера
logging.basicConfig(level=logging.INFO)

# Конфигурация
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Роутеры
dp.include_router(start.router)
dp.include_router(status.router)
dp.include_router(log_work.router)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())