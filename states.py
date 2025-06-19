from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    genre = State()
    years = State()


class Film(StatesGroup):
    name = State()


class New_Film(StatesGroup):
    film = State()
    genre = State()
    year = State()
    country = State()
    director = State()
    about = State()
    photo = State()
