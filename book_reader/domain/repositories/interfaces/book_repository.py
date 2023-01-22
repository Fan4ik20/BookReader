from typing import Protocol

from domain.entities import dto

__all__ = ("BookFileRepository",)


class BookFileRepository(Protocol):
    async def get_by_id(self, user_id: int, book_id: int) -> dto.BookFile | None:
        raise NotImplementedError

    async def create(self, book: dto.BookFileCreate) -> None:
        raise NotImplementedError

    async def delete(self, user_id: int, book_id: int) -> None:
        raise NotImplementedError

    async def update(self, user_id: int, book_id: int, book: dto.BookFileUpdate) -> dto.BookFile | None:
        raise NotImplementedError
