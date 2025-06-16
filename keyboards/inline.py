from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

film_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мелодрама 🥹", callback_data="romance")],
        [InlineKeyboardButton(text="Боевик ⚔️", callback_data="action")],
        [InlineKeyboardButton(text="Комедия 🤪", callback_data="comedy")],
        [InlineKeyboardButton(text="Триллер 💀", callback_data="thriller")],
        [InlineKeyboardButton(text="➡️", callback_data="str2")]
    ]
)

film2_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Документальный 📚", callback_data="documentary")],
        [InlineKeyboardButton(text="Мультфильм 🫅🏼", callback_data="cartoon")],
        [InlineKeyboardButton(text="Детектив 🕵🏻", callback_data="detective")],
        [InlineKeyboardButton(text="Ужасы 👻", callback_data="horror")],
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
        [InlineKeyboardButton(text="80-e", callback_data="eighty"),
         InlineKeyboardButton(text="90-e", callback_data="ninety"),
         InlineKeyboardButton(text="00-e", callback_data="zero"),
         InlineKeyboardButton(text="10-e", callback_data="ten"),
         InlineKeyboardButton(text="20-e", callback_data="twenty")],
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
        [InlineKeyboardButton(text="О боте", callback_data="menu_about")],
        [InlineKeyboardButton(text="⬅️", callback_data="back")]
    ]

)
poisk_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поиск фильмов по критериям", callback_data="menu2_films")],
        [InlineKeyboardButton(text="Рандомный фильм", callback_data="menu2_randfilm")],
        [InlineKeyboardButton(text="Поиск фильмов", callback_data="menu2_poisk")],
        [InlineKeyboardButton(text="⬅️", callback_data="back")]
    ]
)
