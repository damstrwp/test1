from aiogram import Dispatcher, Bot
from config import TOKEN
from handlers.commands import command_router
from handlers.callbacks import callback_router
import asyncio

dp = Dispatcher()  # объявляется диспетчер (класс,который налаживает коммуникацию между мной и тг)
dp.include_router(command_router)
dp.include_router(callback_router)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
