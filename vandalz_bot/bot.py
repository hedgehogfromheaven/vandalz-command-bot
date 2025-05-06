import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from db.postgres import PostgresDB
from handlers import start, status, log_work

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    db = PostgresDB()
    await db.connect()

    dp.include_router(start.router)
    dp.include_router(status.router)
    dp.include_router(log_work.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())