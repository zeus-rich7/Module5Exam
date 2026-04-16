import asyncio
import logging

from aiogram import Dispatcher, Bot

from config import load_config
from src import handlers, middlewares
from src.infrastructure import create_pool, make_connection_string

dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)

    settings = load_config()

    bot = Bot(token=settings.tgbot.token)
    pool = create_pool(url=make_connection_string(settings))

    handlers.setup(dp)
    middlewares.setup(dp, pool)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
