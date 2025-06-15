from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

film_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мелодрама 🥹", callback_data="edit")],
        [InlineKeyboardButton(text="Боевик ⚔️", callback_data="edit")],
        [InlineKeyboardButton(text="Комедия 🤪", callback_data="edit")],
        [InlineKeyboardButton(text="➡️", callback_data="str2")]
    ]
)

film2_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Документальный 📚", callback_data="edit")],
        [InlineKeyboardButton(text="Мультфильм 🫅🏼", callback_data="edit")],
        [InlineKeyboardButton(text="⬅️", callback_data="str1")]
    ]
)

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начнем!", callback_data="start")]
    ]
)

films_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="80-e", callback_data="help"),
         InlineKeyboardButton(text="90-e", callback_data="help"),
         InlineKeyboardButton(text="00-e", callback_data="help"),
         InlineKeyboardButton(text="10-e", callback_data="help"),
         InlineKeyboardButton(text="20-e", callback_data="help"),
         InlineKeyboardButton(text="без годов", callback_data="help")
         ],
        [InlineKeyboardButton(text="⬅️", callback_data="str1")]

    ]
)

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Управление", callback_data="menu"),
         InlineKeyboardButton(text="Поиск фильмов", callback_data="menu2")]
    ]
)
uprav_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Помощь", callback_data="menu_help")],
        [InlineKeyboardButton(text="Меню", callback_data="menu_menu")],
        [InlineKeyboardButton(text="О боте", callback_data="menu_about")]
    ]
)
poisk_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поиск фильмов по критериям", callback_data="menu2_films")],
        [InlineKeyboardButton(text="Рандомный фильм", callback_data="menu2_randfilm")],
        [InlineKeyboardButton(text="Поиск фильмов", callback_data="menu2_poisk")]
    ]
)
