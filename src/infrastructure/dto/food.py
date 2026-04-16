from __future__ import annotations

from src.infrastructure.dto import Base


class Food(Base):
    title: str
    description: str
    category_id: int
