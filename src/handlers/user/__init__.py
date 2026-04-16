from aiogram import Dispatcher

from .main import router as main_menu_router
from .restaurant_menu import router as restaurant_menu_router

def setup(dp: Dispatcher):
    dp.include_router(main_menu_router)
    dp.include_router(restaurant_menu_router)
