from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "/status")
async def status_handler(message: Message):
    await message.answer("✅ Система в порядке. Бот на связи.")