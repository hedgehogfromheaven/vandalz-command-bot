from aiogram import Router, types
from db.postgres import PostgresDB

router = Router()
db = PostgresDB()

@router.message(commands=["status"])
async def status_handler(msg: types.Message):
    name = msg.text.split(" ", 1)[-1] if " " in msg.text else None
    if not name:
        await msg.answer("❗ Use `/status <car_name>`", parse_mode="Markdown")
        return

    status = await db.fetch_vehicle_status(name)
    if status:
        await msg.answer(f"🛠️ *{name}*: {status}", parse_mode="Markdown")
    else:
        await msg.answer(f"🚫 No data for *{name}*", parse_mode="Markdown")