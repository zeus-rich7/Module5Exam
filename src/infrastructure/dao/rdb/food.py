from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure import dto
from src.infrastructure.dao.rdb import BaseDAO
from src.infrastructure.models import Food


class FoodDAO(BaseDAO[Food]):
    def __init__(self, session: AsyncSession):
        super().__init__(Food, session)

    async def add_food(
        self, title: str, description: str, price: int, category_id: int
    ) -> dto.Food:
        food = Food(title=title, description=description, category_id=category_id)
        self.session.add(food)
        await self.session.commit()
        return dto.Food.model_validate(food)

    async def get_food(self, title: str) -> dto.Food | None:
        result = await self.session.execute(
            select(Food).where(Food.title==title)
        )
        food = result.scalar_one_or_none()

        return dto.Food.model_validate(food)


    async def get_foods(self, category_id: int) -> List[dto.Food] | None:
        result = await self.session.execute(
            select(Food).where(Food.category_id==category_id)
        )
        foods = result.scalars()

        return [dto.Food.model_validate(food) for food in foods]
