from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer("🔧 *Vandalz Command Bot Ready*\nUse /status or /log_work to begin.", parse_mode="Markdown")