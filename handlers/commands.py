from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline import film_keyboard, start_keyboard
from keyboards.reply import keyboard
from aiogram.types import FSInputFile
from bd import dct
import random

command_router = Router()


@command_router.message(Command('start'))
async def handle_start(m: Message) -> None:
    photo = FSInputFile("Kinobot.jpg")
    await m.answer_photo(photo, caption="Привет! Это бот для поиска интересных фильмов по вашим интересам.",
                         reply_markup=start_keyboard)


@command_router.message(Command('about'))
async def handle_about(m: Message) -> None:
    about_message = (f"Этот бот ищет фильмы по вашим критериям и выводит их рейтинг.")
    await m.answer(text=about_message)


@command_router.message(or_f(Command('films'), F.text == "Поиск фильмов по критериям"))
async def handle_films(m: Message) -> None:
    films_message = f"Давайте найдем вам фильмы! Выберете ваши интересы."
    await m.answer(text=films_message, reply_markup=film_keyboard)


@command_router.message(or_f(Command("randfilm"), F.text == "Рандомный фильм"))
async def handle_randfilms(m: Message) -> None:
    bd = random.choice(list(dct.items()))
    photo = FSInputFile(bd[1][1])
    text = (f"<b><u>{bd[0]}</u></b>\n"
            f"<i>Краткая информация</i>\n"
            f"{bd[1][0]}")

    await m.answer_photo(photo, caption=text, parse_mode='HTML')


@command_router.message(or_f(Command('film'), F.text == "Поиск фильмов"))
async def handle_film(m: Message) -> None:
    film_message = f"Назовите название фильма и я найду вам информацию  про него."
    await m.answer(text=film_message)


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
                    f"/actor - фильмы с определенным актером ")
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


# @command_router.message(F.sticker)
# async def handle_stiker(m: Message):
#     await m.answer("Какой крутой стикер!")
#
#
# @command_router.message(F.photo)
# async def handler_photo(m: Message):
#     await m.answer("Какое крутое фото!")
#
#
# @command_router.message(F.text.lower().contains("("))
# async def handler_photo(m: Message):
#     await m.answer_sticker("CAACAgIAAxkBAAPbaEwXMaGiAzugE-Z6KbTS1mYGe2oAAiMSAALtuPlInDuNNk72uMM2BA")
#

@command_router.message()
async def echo_message(message: Message) -> None:
    try:
        await message.reply(text=message.text)
    except TypeError:
        await message.answer("Nice try!")
