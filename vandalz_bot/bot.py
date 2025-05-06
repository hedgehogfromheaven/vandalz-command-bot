import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import load_config

config = load_config()

bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message()
async def handle_all_messages(message: Message):
    await message.answer("Vandalz bot is alive and kicking! 🔥")

async def main():
    print("Starting Vandalz bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
