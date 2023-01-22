from typing import Iterable

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities import dto, models
from domain.mappers import BookFileMapper, ModelMapper
from domain.repositories.interfaces import BookFileRepository

from .base import AlchemyRepositoryBase

__all__ = ("BookFileRepositoryImp",)


class BookFileRepositoryImp(AlchemyRepositoryBase, BookFileRepository):
    def __init__(self, session: AsyncSession, mapper: ModelMapper = BookFileMapper()) -> None:
        super().__init__(session, mapper)

    async def get_by_id(self, user_id: int, book_id: int) -> dto.BookFile | None:
        book: models.BookFile = await self._session.scalar(
            select(models.BookFile).filter_by(id=book_id, user_id=user_id)
        )

        return self._mapper.to_repr(book) if book else None

    async def get_list(self, user_id: int, offset: int, limit: int) -> Iterable[dto.BookFile]:
        result = await self._session.scalars(
            select(models.BookFile).filter_by(user_id=user_id).offset(offset).limit(limit)
        )

        return self._mapper.to_repr_list(result.all())

    async def create(self, book: dto.BookFileCreate) -> dto.BookFile:
        book_create: models.BookFile = self._mapper.to_model_create(book)

        self._session.add(book_create)
        await self._session.flush()
        await self._session.refresh(book_create)

        book_dto: dto.BookFile = self._mapper.to_repr(book_create)
        return book_dto

    async def delete(self, user_id: int, book_id: int) -> None:
        await self._session.execute(delete(models.BookFile).filter_by(id=book_id, user_id=user_id))

    async def update(self, user_id: int, book_id: int, book: dto.BookFileUpdate) -> dto.BookFile:
        result = await self._session.scalars(select(models.BookFile).filter_by(id=book_id, user_id=user_id))
        book_model: models.BookFile = result.one()

        self._update_model(book_model, book)

        book_dto: dto.BookFile = self._mapper.to_repr(book_model)
        return book_dto
