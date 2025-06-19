from aiogram import Router
from Middleware import AdminMiddleware
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import New_Film
from database import add_film

admin_router = Router()
admin_router.message.middleware(AdminMiddleware())


@admin_router.message(Command('admin'))
async def admin(m: Message):
    await m.answer(f"/admin_films - добавить новый фильм")


@admin_router.message(Command("admin_films"))
async def get_new_film(m: Message, state: FSMContext):
    await m.answer("Напишите название фильма большой буквы")
    await state.set_state(New_Film.film)


@admin_router.message(New_Film.film)
async def set_film(m: Message, state: FSMContext):
    await state.update_data(film=f"<b><u>{m.text}</u></b>")
    await m.answer("Напишите название жанра с большой буквы")
    await state.set_state(New_Film.genre)


@admin_router.message(New_Film.genre)
async def set_genre(m: Message, state: FSMContext):
    await state.update_data(genre=m.text)
    await m.answer("Напишите года (2020-е) такого типа")
    await state.set_state(New_Film.year)


@admin_router.message(New_Film.year)
async def set_genre(m: Message, state: FSMContext):
    await state.update_data(year=m.text)
    await m.answer("Напишите страну")
    await state.set_state(New_Film.country)


@admin_router.message(New_Film.country)
async def set_genre(m: Message, state: FSMContext):
    await state.update_data(country=m.text)
    await m.answer("Напишите режиссера")
    await state.set_state(New_Film.director)


@admin_router.message(New_Film.director)
async def set_genre(m: Message, state: FSMContext):
    await state.update_data(director=m.text)
    await m.answer("Напишите, о чем фильм")
    await state.set_state(New_Film.about)


@admin_router.message(New_Film.about)
async def set_genre(m: Message, state: FSMContext):
    await state.update_data(about=m.text)
    data = await state.get_data()
    add_film(
        film=data['film'],
        genre=data['genre'],
        year=data['year'],
        country=data['country'],
        director=data['director'],
        about=data['about'],
        photo=""
    )
    await state.clear()
