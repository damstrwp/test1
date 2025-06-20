from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

film_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мелодрама 🥹", callback_data="romance")],
        [InlineKeyboardButton(text="Боевик ⚔️", callback_data="action")],
        [InlineKeyboardButton(text="Комедия 🤪", callback_data="comedy")],
        [InlineKeyboardButton(text="Триллер 💀", callback_data="thriller")],
        [InlineKeyboardButton(text="Фантастика 👽", callback_data="science_fiction")],
        [InlineKeyboardButton(text="Фэнтези 🧚", callback_data="fantasy")],
        [InlineKeyboardButton(text="Драма 😭", callback_data="drama")],
        [InlineKeyboardButton(text="Вперед ➡️", callback_data="str2")]
    ]
)

film2_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Аниме 👾", callback_data="anime")],
        [InlineKeyboardButton(text="Мультфильм 🫅🏼", callback_data="cartoon")],
        [InlineKeyboardButton(text="Детектив 🕵🏻", callback_data="detective")],
        [InlineKeyboardButton(text="Ужасы 👻", callback_data="horror")],
        [InlineKeyboardButton(text="Криминал 💰", callback_data="crime")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="str1")]
    ]
)

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начнем!👀", callback_data="start")]
    ]
)
continue_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продолжим?👀", callback_data="continue")]
    ]
)
random_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Супер!👍", callback_data="random_yes"),
         InlineKeyboardButton(text="Другой фильм👎", callback_data="menu2_randfilm")],
        [InlineKeyboardButton(text="Продолжим?👀", callback_data="continue")]
    ]
)

films_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎥70-e", callback_data="seventy"),
         InlineKeyboardButton(text="🎥80-e", callback_data="eighty"),
         InlineKeyboardButton(text="🎥90-e", callback_data="ninety")],
        [InlineKeyboardButton(text="🎥00-e", callback_data="zero"),
         InlineKeyboardButton(text="🎥10-e", callback_data="ten"),
         InlineKeyboardButton(text="🎥20-e", callback_data="twenty")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="str1")]

    ]
)

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Управление ⚙️", callback_data="menu"),
         InlineKeyboardButton(text="Поиск фильмов 🔍", callback_data="menu2")]
    ]
)
uprav_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Помощь ⚙️", callback_data="menu_help"),
         InlineKeyboardButton(text="Меню 🔠", callback_data="menu_menu"),
         InlineKeyboardButton(text="О боте 🤖", callback_data="menu_about")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]

)
poisk_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поиск фильмов по критериям", callback_data="menu2_films")],
        [InlineKeyboardButton(text="Рандомный фильм", callback_data="menu2_randfilm")],
        [InlineKeyboardButton(text="Поиск фильмов", callback_data="menu2_poisk")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]
)
kriterii_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поиск фильмов по жанрам", callback_data="poisk_genre")],
        [InlineKeyboardButton(text="Поиск фильмов по годам", callback_data="poisk_year")],
        [InlineKeyboardButton(text="Поиск фильмов по жанрам и годам", callback_data="poisk")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back2")]
    ]
)

film_genre_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мелодрама 🥹", callback_data="romance1")],
        [InlineKeyboardButton(text="Боевик ⚔️", callback_data="action1")],
        [InlineKeyboardButton(text="Комедия 🤪", callback_data="comedy1")],
        [InlineKeyboardButton(text="Триллер 💀", callback_data="thriller1")],
        [InlineKeyboardButton(text="Фантастика 👽", callback_data="science_fiction1")],
        [InlineKeyboardButton(text="Фэнтези 🧚", callback_data="fantasy1")],
        [InlineKeyboardButton(text="Драма 😭", callback_data="drama1")],
        [InlineKeyboardButton(text="Вперед ➡️", callback_data="str2_2")]
    ]
)

film2_genre_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Аниме 👾", callback_data="anime1")],
        [InlineKeyboardButton(text="Мультфильм 🫅🏼", callback_data="cartoon1")],
        [InlineKeyboardButton(text="Детектив 🕵🏻", callback_data="detective1")],
        [InlineKeyboardButton(text="Ужасы 👻", callback_data="horror1")],
        [InlineKeyboardButton(text="Криминал 💰", callback_data="crime1")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="str1_2")]
    ]
)

films_year_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎥70-e", callback_data="seventy1"),
         InlineKeyboardButton(text="🎥80-e", callback_data="eighty1"),
         InlineKeyboardButton(text="🎥90-e", callback_data="ninety1"),
         InlineKeyboardButton(text="🎥00-e", callback_data="zero1"),
         InlineKeyboardButton(text="🎥10-e", callback_data="ten1"),
         InlineKeyboardButton(text="🎥20-e", callback_data="twenty1")]

    ]
)
