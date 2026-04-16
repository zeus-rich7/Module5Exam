from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.dao.rdb import BaseDAO, UserDAO, CategoryDAO, FoodDAO


class HolderDAO:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseDAO
        self.user = UserDAO(session=session)
        self.category = CategoryDAO(session=session)
        self.food = FoodDAO(session=session)
