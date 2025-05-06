from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config import load_config
from handlers import start

config = load_config()

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start.router)

async def on_startup():
    print("Bot is starting...")

async def on_shutdown():
    print("Bot is shutting down...")

if __name__ == "__main__":
    import asyncio
    async def main():
        await on_startup()
        await dp.start_polling(bot)
        await on_shutdown()
    asyncio.run(main())