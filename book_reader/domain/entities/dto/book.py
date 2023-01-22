from dataclasses import dataclass
from uuid import UUID

__all__ = (
    "BookFileCreate",
    "BookFileUpdate",
    "BookFile",
)


@dataclass(frozen=True)
class BookFile:
    id: UUID
    title: str
    author: str | None
    user_id: int


@dataclass(frozen=True)
class BookFileCreate:
    title: str
    author: str | None
    user_id: int


@dataclass(frozen=True)
class BookFileUpdate:
    title: str
    author: str | None
