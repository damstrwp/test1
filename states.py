from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    genre = State()
    years = State()


class Film(StatesGroup):
    name = State()
