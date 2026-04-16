from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.helpers.states.user import FoodMenuStates
from src.infrastructure.dao import HolderDAO
from src.keyboards.user.reply_markup import main_menu

router = Router()

@router.message(F.text == "🔙 Orqaga", StateFilter(FoodMenuStates.food))
@router.message(CommandStart())
async def start_handler(msg: Message, dao: HolderDAO):
    user = await dao.user.get_user_by_telegram_id(telegram_id=msg.from_user.id)
    if not user:
        await dao.user.add_user(telegram_id=msg.from_user.id)

    await msg.answer(
        text="Asosiy Menyu",
        reply_markup=main_menu())

@router.message(F.text == "📞 Biz bilan aloqa")
async def contact_handler(msg: Message):
    await msg.answer(
        text="🖇 Telegram: @username\n"
             "☎️ Telefon: +998 90 123 4567")
