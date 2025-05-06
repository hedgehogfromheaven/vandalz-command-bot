from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer("✅ Bot is up and running.")