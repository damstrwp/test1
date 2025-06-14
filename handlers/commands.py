from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import F
from keyboards.inline import film_keyboard
import random

command_router = Router()


@command_router.message(Command('start'))
async def handle_start(m: Message) -> None:
    start_message = (f"Привет! Это бот для поиска интересных фильмов по вашим интересам.\n"
                     f"Нажми на /help ,чтобы узнать о командах,которые я умею.")
    await m.answer(text=start_message)


@command_router.message(Command('about'))
async def handle_about(m: Message) -> None:
    about_message = (f"Этот бот ищет фильмы по вашим критериям и выводит их рейтинг.")
    await m.answer(text=about_message)


@command_router.message(Command('films'))
async def handle_films(m: Message) -> None:
    films_message = (f"Давайте найдем вам фильмы! Выберете ваши интересы.")
    await m.answer(text=films_message,reply_markup=film_keyboard)


@command_router.message(Command("actor"))
async def handle_actors(m: Message) -> None:
    actors_message = (f"Назовите актера и я найду фильмы с ним.")
    await m.answer(text=actors_message)


@command_router.message(Command('film'))
async def handle_film(m: Message) -> None:
    film_message = (f"Назовите название фильма и я найду вам информацию  про него.")
    await m.answer(text=film_message)


@command_router.message(Command('help'))
async def handle_help(m: Message) -> None:
    help_message = (f"Я всегда готов помочь! \n"
                    f"Управление:\n"
                    f"/start - начало работы \n"
                    f"/help - навигация \n"
                    f"/about - расскажет о чем этот бот \n"
                    f"Поиск фильма:\n"
                    f"/films - найти фильмы по критериям \n"
                    f"/film - поиск определенного фильма по названию\n"
                    f"/actor - фильмы с определенным актером ")
    await m.answer(text=help_message)


@command_router.message(F.text.lower().in_(["привет", "здравствуйте", "хай"]))
async def handle_hi(m: Message):
    hello = ["Привет!❤️\nНужна помощь с фильмами?🎥", "Привет-привет!🤗\nИщешь подхдящий фильм?🍿"]
    await m.answer(text=hello[random.randint(0, len(hello) - 1)])


@command_router.message(F.text.lower().in_(["пока", "до свидания","бай"]))
async def handle_bye(m: Message):
    byes = ["До новых встреч!😌", "Пока-пока!😉", "До свидания! 😊"]
    await m.answer(text=byes[random.randint(0, len(byes) - 1)])


@command_router.message(F.text.lower.in_("❤️"))
async def handle_heart(m: Message):
    await m.answer("Спасибо за сердечко!Был рад помочь!")


@command_router.message(F.sticker)
async def handle_stiker(m: Message):
    await m.answer("Какой крутой стикер!")


@command_router.message(F.photo)
async def handler_photo(m: Message):
    await m.answer("Какое крутое фото!")


@command_router.message(F.text.lower().contains("("))
async def handler_photo(m: Message):
    await m.answer_sticker("CAACAgIAAxkBAAPbaEwXMaGiAzugE-Z6KbTS1mYGe2oAAiMSAALtuPlInDuNNk72uMM2BA")


@command_router.message()
async def echo_message(message: Message) -> None:
    try:
        await message.reply(text=message.text)
    except TypeError:
        await message.answer("Nice try!")
