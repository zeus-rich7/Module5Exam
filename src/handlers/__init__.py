from aiogram import Dispatcher
from src.handlers import admin
from src.handlers import user

def setup(dp: Dispatcher):
    # TODO: Admin handlers setup
    user.setup(dp)
