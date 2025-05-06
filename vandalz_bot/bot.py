import asyncio
from aiogram import Bot, Dispatcher, types

# Hardcoded config (replace with your token)
API_TOKEN = "8156758624:AAGQCAHhTkTWIaeKNA2RO9drnTiEbh-UdqQ"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer(f"👋 You said: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
