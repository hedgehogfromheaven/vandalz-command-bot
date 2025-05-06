# handlers/basic.py

from aiogram import types, Dispatcher


async def cmd_start(message: types.Message):
    await message.answer("👋 Добро пожаловать в Vandalz Bot. Готов к бою.")


async def echo_handler(message: types.Message):
    await message.answer(f"🔁 Ты сказал: {message.text}")


def register_basic_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, commands={"start"})
    dp.message.register(echo_handler)
