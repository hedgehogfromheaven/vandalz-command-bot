from aiogram.fsm.state import State, StatesGroup

class LogWorkFSM(StatesGroup):
    car = State()
    action = State()
    member = State()
    notes = State()