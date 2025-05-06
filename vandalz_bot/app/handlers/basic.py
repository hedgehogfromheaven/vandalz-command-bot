from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("🚗 *Vandalz Ops Bot Ready.*\nUse /addcar or /logaction to begin.")