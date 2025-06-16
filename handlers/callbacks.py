import aiogram
from aiogram import F, Router
from keyboards.inline import films_keyboard, film2_keyboard, film_keyboard, menu_keyboard, uprav_keyboard, \
    poisk_keyboard
from aiogram.types import ReplyKeyboardRemove
from handlers.commands import handle_films, handle_film, handle_randfilms, handle_help, handle_menu, handle_about
from aiogram.fsm.context import FSMContext
from states import Form

callback_router = Router()


@callback_router.callback_query(F.data == "help")
async def handle_helpbutton(callback: aiogram.types.CallbackQuery):
    await callback.answer("Уже спешу помочь!")
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
    await callback.message.answer(text=help_message, parse_mode="HTML")


@callback_router.callback_query(F.data == "about")
async def handle_aboutbutton(callback: aiogram.types.CallbackQuery):
    await callback.answer("О нас")
    await callback.message.answer(f"Этот бот ищет фильмы по вашим критериям и выводит их рейтинг.")


@callback_router.callback_query(
    F.data.in_({"romance", "action", "comedy", "thriller", "documentary", "cartoon", "detective", "horror"}))
async def handle_genre(callback: aiogram.types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Form.genre)
    await state.update_data(genre=callback.data)
    await callback.message.edit_text(text="Выберите десятилетие", reply_markup=films_keyboard)


@callback_router.callback_query(
    F.data.in_({"eighty", "ninety", "zero", "ten", "twenty"}))
async def handle_year(callback: aiogram.types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Form.years)
    await state.update_data(years=callback.data)
    data = await state.get_data()
    await callback.message.answer(text=f"Жанр: {data['genre']}, Года: {data['years']}")
    await state.clear()
    await handle_randfilms(callback.message)
    await callback.message.edit_text(text="Вот список фильмов по вашим критериям:", reply_markup=None)


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


@callback_router.callback_query(F.data == "start")
async def handle_start(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption=f"Привет,{callback.from_user.username}! Это бот для поиска интересных фильмов по вашим интересам.",
                                        reply_markup=None)
    await callback.message.answer(f"С чего начнем?", reply_markup=menu_keyboard)


@callback_router.callback_query(F.data == "continue")
async def handle_start(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"С чего начнем?", reply_markup=menu_keyboard)


@callback_router.callback_query(F.data == "menu")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите функцию", reply_markup=uprav_keyboard)


@callback_router.callback_query(F.data == "menu2")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите функцию", reply_markup=poisk_keyboard)


@callback_router.callback_query(F.data == "menu2_films")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_films(callback.message)


@callback_router.callback_query(F.data == "menu2_poisk")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_film(callback.message)


@callback_router.callback_query(F.data == "menu2_randfilm")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_randfilms(callback.message)


@callback_router.callback_query(F.data == "menu_help")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_help(callback.message)


@callback_router.callback_query(F.data == "menu_menu")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_menu(callback.message)


@callback_router.callback_query(F.data == "menu_about")
async def handle_message(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await handle_about(callback.message)


@callback_router.callback_query(F.data == "back")
async def handle_back(callback: aiogram.types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите функцию", reply_markup=menu_keyboard)
