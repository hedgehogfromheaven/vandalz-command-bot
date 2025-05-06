import asyncio
from aiogram import Bot, Dispatcher

# сюда вставляешь токен напрямую или из переменной окружения
BOT_TOKEN = "8156758624:AAFcIcItUe7jK_XjLoFbtrvuHxjy7fWeTBU"

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    # тут твои хендлеры

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
