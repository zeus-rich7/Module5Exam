from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models import BaseModel


class Category(BaseModel):

    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(VARCHAR(30), unique=True)