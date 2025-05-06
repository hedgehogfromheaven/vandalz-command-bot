# vandalz_bot/bot.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from handlers.echo import router as echo_router
import logging
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

# Init logging
logging.basicConfig(level=logging.INFO)

# Init bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher()
dp.include_router(echo_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
