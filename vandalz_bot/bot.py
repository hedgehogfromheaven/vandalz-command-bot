import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# Получение токена из окружения
API_TOKEN = os.getenv("BOT_TOKEN")
if not API_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables")

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Хэндлер для всех входящих сообщений
@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer(f"👋 You said: {message.text}")

# Основной запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
