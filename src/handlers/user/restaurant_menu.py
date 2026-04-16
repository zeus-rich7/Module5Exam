from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.helpers.states.user import FoodMenuStates
from src.infrastructure.dao import HolderDAO

router = Router()

@router.message(F.text == "🔙 Orqaga", StateFilter(FoodMenuStates.recipie))
@router.message(F.text == "🍽 Restoran menyusi")
async def restaurant_menu_handler(msg: Message, state: FSMContext, dao: HolderDAO):
    categories = await dao.category.get_categories()

    rkb = ReplyKeyboardBuilder()
    for category in categories:
        rkb.add(KeyboardButton(text=category.title))
    rkb.add(KeyboardButton(text="🔙 Orqaga"))
    rkb.adjust(2,1,1)
    markup = rkb.as_markup(resize_keyboard=True)

    await msg.answer(
        text="🍽 Restoran menyusi:",
        reply_markup=markup
    )
    await state.set_state(FoodMenuStates.food)

@router.message(StateFilter(FoodMenuStates.food))
async def category_handler(msg: Message, state: FSMContext, dao: HolderDAO):
    category = await dao.category.get_category(msg.text)
    if not category or not msg.text:
        await msg.answer("Bunday kategoriya mavjud emas. Iltimos menyudan tanlang!")
        return
    foods = await dao.food.get_foods(category.id)

    rkb = ReplyKeyboardBuilder()
    for food in foods:
        rkb.add(KeyboardButton(text=food.title))
    rkb.add(KeyboardButton(text="🔙 Orqaga"))
    rkb.adjust(2, repeat=True)
    markup = rkb.as_markup(resize_keyboard=True)

    await msg.answer(
        text=msg.text,
        reply_markup=markup
    )
    await state.set_state(FoodMenuStates.recipie)



@router.message(StateFilter(FoodMenuStates.recipie))
async def category_handler(msg: Message, dao: HolderDAO):
    food = await dao.food.get_food(msg.text)
    await msg.answer(
        text=food.description,
    )
