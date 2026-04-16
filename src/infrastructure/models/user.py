from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models import BaseModel


class User(BaseModel):

    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)