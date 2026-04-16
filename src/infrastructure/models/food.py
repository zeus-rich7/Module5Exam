from sqlalchemy import VARCHAR, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models import BaseModel


class Food(BaseModel):

    __tablename__ = "foods"

    title: Mapped[str] = mapped_column(VARCHAR(60))
    description: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer)
