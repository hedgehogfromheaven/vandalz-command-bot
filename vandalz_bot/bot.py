import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import asyncio

# Загружаем .env
load_dotenv("/app/.env")  # Укажи абсолютный путь, если билдит контейнер

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing from .env")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Echo: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
