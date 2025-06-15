from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Поиск фильмов по критериям")],
        [KeyboardButton(text="Рандомный фильм")],
        [KeyboardButton(text="Поиск фильмов"), KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True

)
