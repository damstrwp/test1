import aiogram
from aiogram import F, Router
from keyboards.inline import films_keyboard, film2_keyboard, film_keyboard, menu_keyboard, uprav_keyboard, \
    poisk_keyboard, continue_keyboard
from aiogram.types import ReplyKeyboardRemove
from handlers.commands import handle_films, handle_film, handle_randfilms, handle_help, handle_menu, handle_about
from aiogram.fsm.context import FSMContext
from states import Form
from database import get_film

callback_router = Router()


@callback_router.callback_query(F.data == "start")  # после нажатия кнопки "Начнем!"
async def handle_start(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(
        caption=f"Привет, {callback.from_user.username}! Это бот для поиска интересных фильмов по вашим интересам.",
        reply_markup=None)
    await callback.message.answer(f"С чего начнем?", reply_markup=menu_keyboard)


@callback_router.callback_query(F.data == "menu")  # нажатие кнопки "Управление"
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите функцию", reply_markup=uprav_keyboard)


@callback_router.callback_query(F.data == "menu_help")  # кнопка помощь
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_help(callback.message)  # ссылаюсь на функцию из commands


@callback_router.callback_query(F.data == "menu_about")  # при нажатии кнопки "о боте",выводится информация о нем
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_about(callback.message)


@callback_router.callback_query(F.data == "menu_menu")  # кнопка меню,выводит реплай клавиатуру
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_menu(callback.message)


@callback_router.callback_query(F.data == "menu2")  # после нажатия кнопки поиск фильмов
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите функцию", reply_markup=poisk_keyboard)


@callback_router.callback_query(F.data == "menu2_films")  # фильмы по критериям
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_films(callback.message)


@callback_router.callback_query(F.data == "menu2_poisk")  # по названию
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_film(callback.message)


@callback_router.callback_query(F.data == "menu2_randfilm")  # рандоиный фильм
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_randfilms(callback.message)


@callback_router.callback_query(
    F.data.in_(
        {"romance", "action", "comedy", "thriller", "documentary", "cartoon", "detective", "horror", "science_fiction",
         "family", "crime", "fantasy", "drama"}))
async def handle_genre(callback: aiogram.types.CallbackQuery, state: FSMContext):
    await callback.answer()
    genre = callback.data
    genre_ru = ""
    match genre:
        case "romance":
            genre_ru = "Мелодрама"
        case "action":
            genre_ru = "Боевик"
        case "comedy":
            genre_ru = "Комедия"
        case "thriller":
            genre_ru = "Триллер"
        case "documentary":
            genre_ru = "Исторический"
        case "cartoon":
            genre_ru = "Мультфильм"
        case "detective":
            genre_ru = "Детектив"
        case "horror":
            genre_ru = "Ужасы"
        case "family":
            genre_ru = "Семейный"
        case "science_fiction":
            genre_ru = "Фантастика"
        case "fantasy":
            genre_ru = "Фэнтези"
        case "crime":
            genre_ru = "Криминал"
        case "drama":
            genre_ru = "Драма"

    await state.set_state(Form.genre)
    await state.update_data(genre=genre_ru)
    await callback.message.edit_text(text="Выберите десятилетие", reply_markup=films_keyboard)


@callback_router.callback_query(
    F.data.in_({"seventy", "eighty", "ninety", "zero", "ten", "twenty"}))
async def handle_year(callback: aiogram.types.CallbackQuery, state: FSMContext):
    await callback.answer()
    year = callback.data
    year_ru = ""
    match year:
        case "seventy":
            year_ru = "1970-е"
        case "eighty":
            year_ru = "1980-е"
        case "ninety":
            year_ru = "1990-е"
        case "zero":
            year_ru = "2000-е"
        case "ten":
            year_ru = "2010-е"
        case "twenty":
            year_ru = "2020-е"

    await state.set_state(Form.years)
    await state.update_data(years=year_ru)
    data = await state.get_data()
    await callback.message.edit_text(
        text=f"Вот список фильмов по вашим критериям (жанр: {data['genre']}, года: {data['years']}):",
        reply_markup=None)
    spisok = get_film(genre=data['genre'], year=data['years'])
    formatted_output = ""
    for i, film in enumerate(spisok, 1):
        title, genre, year, country, director, about = film
        formatted_output += f"{i}. {title}\nЖанр: {genre}\nГод: {year}\nСтрана: {country}\nРежиссер: {director}\nКраткое описание: {about}\n\n"
    await callback.message.answer(text=formatted_output.strip(), parse_mode='HTML', reply_markup=continue_keyboard)
    await state.clear()


@callback_router.callback_query(F.data == "str2")
async def handle_arrow(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text=f"Давайте найдем вам фильмы! Выберите жанр.",
                                     reply_markup=film2_keyboard)


@callback_router.callback_query(F.data == "str1")
async def handle_arrow(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Давайте найдем вам фильмы! Выберите жанр.",
                                     reply_markup=film_keyboard)


@callback_router.callback_query(F.data == "continue")
async def handle_start(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"С чего начнем?", reply_markup=menu_keyboard)


@callback_router.callback_query(F.data == "back")
async def handle_back(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите функцию", reply_markup=menu_keyboard)
