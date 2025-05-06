
from config import load_config
from aiogram import Bot, Dispatcher
import asyncio

# Load config (stub for now)
config = load_config()

bot = Bot(token=config.bot_token)
dp = Dispatcher()

async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
