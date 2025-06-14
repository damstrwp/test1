import aiogram
from aiogram import F, Router

callback_router = Router()


@callback_router.callback_query(F.data == "help")
async def handle_helpbutton(callback: aiogram.types.CallbackQuery):
    await callback.answer("Уже спешу помочь!")
    await callback.message.answer(f"Я всегда готов помочь! \n"
                                  f"Управление:\n"
                                  f"/start - начало работы \n"
                                  f"/help - навигация \n"
                                  f"/about - расскажет о чем этот бот \n"
                                  f"Поиск фильма:\n"
                                  f"/films - найти фильмы по критериям \n"
                                  f"/film - поиск определенного фильма по названию\n"
                                  f"/actor - фильмы с определенным актером ")


@callback_router.callback_query(F.data == "about")
async def handle_aboutbutton(callback: aiogram.types.CallbackQuery):
    await callback.answer("О нас")
    await callback.message.answer(f"Этот бот ищет фильмы по вашим критериям и выводит их рейтинг.")
