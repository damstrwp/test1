from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

film_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мелодрама 🥹", url="https://ru.kinorium.com/108983/"),
         InlineKeyboardButton(text="Боевик ⚔️", url="https://ru.kinorium.com/116780/"),
         InlineKeyboardButton(text="Комедия 🤪", url="https://ru.kinorium.com/537521/")],
        [InlineKeyboardButton(text="Документальный 📚", url="https://ru.kinorium.com/1676875/"),
         InlineKeyboardButton(text="Мультфильм 🫅🏼", url="https://ru.kinorium.com/112655/")],
        [InlineKeyboardButton(text="Помощь ⚙️",callback_data="help")]
    ]
)

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Помощь ⚙️",callback_data="help")]
    ]
)
