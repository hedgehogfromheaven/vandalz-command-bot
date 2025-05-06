# vandalz_bot/bot.py

import asyncio
from aiogram import Bot, Dispatcher
from vandalz_bot.config import load_config
from vandalz_bot.handlers import setup_handlers


async def main():
    # Загружаем конфиг
    config = load_config()

    # Создаём бота и диспетчер
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    # Подключаем все хендлеры
    setup_handlers(dp)

    # Запускаем поллинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
