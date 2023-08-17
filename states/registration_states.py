from aiogram .dispatcher.filters.state import State, StatesGroup

class Registration(StatesGroup):
    enter_name = State()
    enter_email = State()
    enter_age = State()
    profile = State()
    set_new_name = State()
    set_new_email = State()
    set_new_age = State()