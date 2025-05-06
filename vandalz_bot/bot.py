from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

from vandalz_bot.config import load_config

# Load token from .env
config = load_config()
BOT_TOKEN = config.vandalz_token

if not BOT_TOKEN:
    raise RuntimeError("VANDALZ_TOKEN is missing from .env")

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.answer("🚀 VANDALZ BOT ready to serve.")

if __name__ == "__main__":
    import asyncio
    async def main():
        await dp.start_polling(bot)
    asyncio.run(main())
