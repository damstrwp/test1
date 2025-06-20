from aiogram import Dispatcher, Bot
from config import TOKEN
from handlers.commands import command_router
from handlers.callbacks import callback_router
from handlers.admin import admin_router
from aiogram.fsm.storage.memory import MemoryStorage
from Middleware import AntiFloodMiddleware
import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=None
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # объявляется диспетчер (класс,который налаживает коммуникацию между мной и тг)
dp.message.middleware(AntiFloodMiddleware(delay=2.0))

dp.include_router(command_router)
dp.include_router(callback_router)
dp.include_router(admin_router)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
