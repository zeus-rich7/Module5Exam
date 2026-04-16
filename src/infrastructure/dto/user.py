from __future__ import annotations

from src.infrastructure.dto import Base


class User(Base):
    telegram_id: int
