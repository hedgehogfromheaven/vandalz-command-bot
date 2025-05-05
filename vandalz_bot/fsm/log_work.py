from aiogram.fsm.state import StatesGroup, State

class LogWorkFSM(StatesGroup):
    car = State()
    action = State()
    member = State()
    notes = State()