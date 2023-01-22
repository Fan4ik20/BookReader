from typing import Iterable

from domain.entities import dto
from .base import ServiceBase

from services.interfaces import BookFileService
from services import exc

from domain.repositories.interfaces import BookFileRepository, UserRepository
from domain.repositories.uow import UOW


class BookFileServiceImp(ServiceBase[BookFileRepository], BookFileService):
    def __init__(self, repo: BookFileRepository, uow: UOW, user_repo: UserRepository) -> None:
        self._user_repo = user_repo
        super().__init__(repo, uow)

    async def _raise_exc_if_user_is_none(self, user_id: int) -> None:
        if not await self._user_repo.get_by_id(user_id):
            raise exc.UserNotFound

    async def get_by_id(self, user_id: int, book_id: int) -> dto.BookFile:
        await self._raise_exc_if_user_is_none(user_id)

        book = await self._repo.get_by_id(user_id, book_id)

        if not book:
            raise exc.BookFileNotFound

        return book

    async def get_list(self, user_id: int, offset: int = 0, limit: int = 100) -> Iterable[dto.BookFile]:
        await self._raise_exc_if_user_is_none(user_id)

        return await self._repo.get_list(user_id, offset, limit)

    async def update(self, user_id: int, book_id: int, book: dto.BookFileUpdate) -> dto.BookFile:
        await self._raise_exc_if_user_is_none(user_id)

        if not await self._repo.get_by_id(user_id, book_id):
            raise exc.BookFileNotFound

        with self._uow:
            return await self._repo.update(user_id, book_id, book)

    async def delete(self, user_id: int, book_id: int) -> None:
        await self._raise_exc_if_user_is_none(user_id)

        with self._uow:
            await self._repo.delete(user_id, book_id)

    async def create(self, book: dto.BookFileCreate) -> dto.BookFile:
        await self._raise_exc_if_user_is_none(book.user_id)

        with self._uow:
            return await self._repo.create(book)
