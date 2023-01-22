from typing import Protocol, Iterable

from domain.entities import dto


__all__ = ("BookFileService",)


class BookFileService(Protocol):
    async def get_by_id(self, user_id: int, book_id: int) -> dto.BookFile:
        raise NotImplementedError

    async def get_list(self, user_id: int, offset: int = 0, limit: int = 100) -> Iterable[dto.BookFile]:
        raise NotImplementedError

    async def update(self, user_id: int, book_id: int, book: dto.BookFileUpdate) -> dto.BookFile:
        raise NotImplementedError

    async def delete(self, user_id: int, book_id: int) -> None:
        raise NotImplementedError

    async def create(self, book: dto.BookFileCreate) -> dto.BookFile:
        raise NotImplementedError
