from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from fsm.log_work import LogWorkFSM
from db.postgres import PostgresDB

router = Router()
db = PostgresDB()

@router.message(Command("log_work"))
async def start_log(msg: types.Message, state: FSMContext):
    await msg.answer("📋 Enter car name:")
    await state.set_state(LogWorkFSM.car)

@router.message(LogWorkFSM.car)
async def log_car(msg: types.Message, state: FSMContext):
    await state.update_data(car=msg.text)
    await msg.answer("🔧 Enter action performed:")
    await state.set_state(LogWorkFSM.action)

@router.message(LogWorkFSM.action)
async def log_action(msg: types.Message, state: FSMContext):
    await state.update_data(action=msg.text)
    await msg.answer("👤 Enter your name:")
    await state.set_state(LogWorkFSM.member)

@router.message(LogWorkFSM.member)
async def log_member(msg: types.Message, state: FSMContext):
    await state.update_data(member=msg.text)
    await msg.answer("📝 Add notes:")
    await state.set_state(LogWorkFSM.notes)

@router.message(LogWorkFSM.notes)
async def log_notes(msg: types.Message, state: FSMContext):
    data = await state.update_data(notes=msg.text)
    await db.insert_log(**data)
    await msg.answer("✅ *Log saved*", parse_mode="Markdown")
    await state.clear()