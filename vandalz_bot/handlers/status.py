from aiogram import Router, types
from aiogram.filters import Command
from db.postgres import PostgresDB

router = Router()
db = PostgresDB()

@router.message(Command("status"))
async def status_handler(msg: types.Message):
    parts = msg.text.split(" ", 1)
    name = parts[1] if len(parts) > 1 else None
    if not name:
        await msg.answer("❗ Use `/status <car_name>`", parse_mode="Markdown")
        return
    status = await db.fetch_vehicle_status(name)
    if status:
        await msg.answer(f"🛠️ *{name}*: {status}", parse_mode="Markdown")
    else:
        await msg.answer(f"🚫 No data for *{name}*", parse_mode="Markdown")