# bot.py
from aiogram import Bot, Dispatcher
from config import load_config
from handlers import basic  # Импортируем твои хендлеры

config = load_config()
bot = Bot(token=config.bot_token)
dp = Dispatcher()

dp.include_router(basic.router)  # Регистрируем хендлеры

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
