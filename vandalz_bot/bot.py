import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from handlers import echo

async def main():
    config = load_config()
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    dp.include_router(echo.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
