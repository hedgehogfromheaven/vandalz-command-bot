from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.startswith("/log "))
async def log_work_handler(message: Message):
    log_text = message.text[5:]
    await message.answer(f"📝 Записано: {log_text}")