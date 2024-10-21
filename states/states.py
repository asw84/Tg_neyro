from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    CHOOSE_DIRECTION = State()
    CHOOSE_LEVEL = State()
    COURSE_ACTION = State()
