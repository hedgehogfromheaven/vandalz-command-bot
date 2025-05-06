from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from app.config import settings

bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("🚗 *Vandalz Ops Bot Ready.*\nUse /addcar or /logaction to begin.")

if __name__ == "__main__":
    import asyncio
    async def main():
        await dp.start_polling(bot)
    asyncio.run(main())
