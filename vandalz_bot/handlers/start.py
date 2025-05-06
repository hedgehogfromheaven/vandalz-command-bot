from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("👊 Добро пожаловать в Vandalz Bot. Мы готовы к старту.")