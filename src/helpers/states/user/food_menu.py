from aiogram.fsm.state import StatesGroup, State


class FoodMenuStates(StatesGroup):
    category = State()
    food = State()
    recipie = State()
