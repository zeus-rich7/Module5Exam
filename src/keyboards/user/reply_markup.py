from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text="🍽 Restoran menyusi"))
    rkb.add(KeyboardButton(text="📞 Biz bilan aloqa"))
    rkb.adjust(2)
    return rkb.as_markup(resize_keyboard=True)
