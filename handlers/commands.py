from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline import film_keyboard, start_keyboard, continue_keyboard, film_genre_keyboard, films_year_keyboard
from keyboards.reply import keyboard
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from database import get_randfilm, get_film_name, get_photo
from states import Film
import random

command_router = Router()


@command_router.message(Command('start'))
async def handle_start(m: Message) -> None:
    photo = FSInputFile("img/Kinobot.jpg")
    await m.answer_photo(photo,
                         caption=f"Привет,  {m.from_user.username}! Это бот для поиска интересных фильмов по вашим интересам.",
                         reply_markup=start_keyboard)


@command_router.message(Command('about'))
async def handle_about(m: Message) -> None:
    about_message = "Этот бот ищет фильмы по вашим критериям и выводит их рейтинг."
    photo = FSInputFile("img/about.jpg")
    await m.answer_photo(photo=photo, caption=about_message)


@command_router.message(or_f(Command('genre'), F.text == "Поиск фильмов по жанрам"))
async def handle_films_genre(m: Message) -> None:
    films_message = "Давайте найдем вам фильмы! Выберете жанр."
    await m.answer(text=films_message, reply_markup=film_genre_keyboard)


@command_router.message(or_f(Command('year'), F.text == "Поиск фильмов по годам"))
async def handle_films_year(m: Message) -> None:
    films_message = "Давайте найдем вам фильмы! Выберете жанр."
    await m.answer(text=films_message, reply_markup=films_year_keyboard)


@command_router.message(or_f(Command('genre_year'), F.text == "Поиск фильмов по жанрам и годам"))
async def handle_films(m: Message) -> None:
    films_message = "Давайте найдем вам фильмы! Выберете жанр."
    await m.answer(text=films_message, reply_markup=film_keyboard)


@command_router.message(or_f(Command("randfilm"), F.text == "Рандомный фильм"))
async def handle_randfilms(m: Message) -> None:
    id = random.randint(1, 13)
    spisok = get_randfilm(id=id)
    print(spisok)
    gph = get_photo(id=id)
    photo = FSInputFile(gph[0][0])
    formatted_output = ""
    for i, film in enumerate(spisok, 1):
        title, genre, year, country, director, about = film
        formatted_output = f"{title}\n<i>Жанр:</i> {genre}\n<i>Год:</i> {year}\n<i>Страна:</i> {country}\n<i" \
                           f">Режиссер:</i> {director}\n<i>Краткое описание:</i> {about}\n\n"
    await m.answer_photo(caption=formatted_output.strip(), photo=photo, parse_mode='HTML',
                         reply_markup=continue_keyboard)


@command_router.message(or_f(Command('film'), F.text == "Поиск фильмов"))
async def handle_film(m: Message, state: FSMContext) -> None:
    film_message = f"Напишите название фильма и я найду вам информацию  про него."
    await m.answer(text=film_message)
    await state.set_state(Film.name)


@command_router.message(Film.name)
async def find_film(m: Message, state: FSMContext):
    await state.update_data(name=m.text)
    data = await state.get_data()
    spisok = get_film_name(f"<b><u>{data['name']}</u></b>")
    print(spisok)
    formatted_output = ""
    for i, film in enumerate(spisok, 1):
        title, genre, year, country, director, about = film
        formatted_output = f"{title}\n<i>Жанр:</i> {genre}\n<i>Год:</i> {year}\n<i>Страна:</i> {country}\n<i" \
                           f">Режиссер:</i> {director}\n<i>Краткое описание:</i> {about}\n\n"
    await m.answer(text=formatted_output.strip(), parse_mode='HTML',
                   reply_markup=continue_keyboard)
    await state.clear()


@command_router.message(Command('menu'))
async def handle_menu(m: Message) -> None:
    await m.answer(text="Выберите функцию из предложенных", reply_markup=keyboard)


@command_router.message(or_f(Command('help'), F.text == "Помощь"))
async def handle_help(m: Message) -> None:
    help_message = (f"<b>Я всегда готов помочь!</b> \n"
                    f"<i>Управление:</i>\n"
                    f"/start - начало работы \n"
                    f"/help - навигация \n"
                    f"/menu  - меню \n"
                    f"/about - расскажет о чем этот бот \n"
                    f"<i>Поиск фильма:</i>\n"
                    f"/films - найти фильмы по критериям \n"
                    f"/film - поиск определенного фильма по названию\n"
                    f"/randfilm - Рандомный фильм ")
    await m.answer(text=help_message, parse_mode="HTML", reply_markup=ReplyKeyboardRemove())


@command_router.message(F.text.lower().in_(["привет", "здравствуйте", "хай"]))
async def handle_hi(m: Message):
    hello = [f"Привет,{m.from_user.username}!❤️\nНужна помощь с фильмами?🎥",
             f"Привет-привет,{m.from_user.username}!🤗\nИщешь подхдящий фильм?🍿"]
    await m.answer(text=hello[random.randint(0, len(hello) - 1)])


@command_router.message(F.text.lower().in_(["пока", "до свидания", "бай"]))
async def handle_bye(m: Message):
    byes = ["До новых встреч!😌", "Пока-пока!😉", "До свидания! 😊"]
    await m.answer(text=byes[random.randint(0, len(byes) - 1)])


@command_router.message()
async def echo_message(message: Message) -> None:
    try:
        await message.reply(text=message.text)
    except TypeError:
        await message.answer("Nice try!")
