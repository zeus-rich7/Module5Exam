from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from src.middlewares.session_manager import HolderMiddleware


def setup(dp: Dispatcher, pool: sessionmaker):
    dp.update.middleware(HolderMiddleware(pool=pool))
    