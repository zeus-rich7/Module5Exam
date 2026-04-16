from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure import dto
from src.infrastructure.dao.rdb import BaseDAO
from src.infrastructure.models import Category


class CategoryDAO(BaseDAO[Category]):
    def __init__(self, session: AsyncSession):
        super().__init__(Category, session)

    async def add_category(
        self, title: str
    ) -> dto.Category:
        category = Category(title=title)
        self.session.add(category)
        await self.session.commit()
        return dto.Category.model_validate(category)

    async def get_category(self, title: str) -> dto.Category | None:
        result = await self.session.execute(
            select(Category).where(Category.title == title)
        )
        category = result.scalar_one_or_none()

        if category:
            return dto.Category.model_validate(category)
        else:
            return None


    async def get_categories(self) -> List[dto.Category]:
        result = await self.session.execute(
            select(Category)
        )
        categories = result.scalars()

        return [dto.Category.model_validate(category) for category in categories]
