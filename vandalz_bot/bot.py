import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Получение токена из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Простейший обработчик
@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты сказал: {message.text}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
