# vandalz_bot/handlers/commands.py
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("🚀 Welcome to Vandalz Bot. Type anything and I’ll echo it back!")

@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("🛠 Commands:\n/start – launch bot\n/help – show this help\nAnything else – I'll echo it.")
