from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Поиск фильмов по жанрам")],
        [KeyboardButton(text="Поиск фильмов по годам")],
        [KeyboardButton(text="Поиск фильмов по жанрам и годам")],
        [KeyboardButton(text="Рандомный фильм")],
        [KeyboardButton(text="Поиск фильмов"), KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True

)
