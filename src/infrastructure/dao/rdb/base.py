from typing import TypeVar, Type, Generic

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.models import Base

Model = TypeVar("Model", Base, Base)


class BaseDAO(Generic[Model]):
    def __init__(
        self,
        model: Type[Model],
        session: AsyncSession,
    ):
        self.model = model
        self.session = session