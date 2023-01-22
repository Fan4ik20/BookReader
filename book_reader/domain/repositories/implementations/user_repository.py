from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities import dto, models
from domain.repositories.interfaces import UserRepository

from .base import AlchemyRepositoryBase

__all__ = ("UserRepositoryImp",)

from domain.mappers import ModelMapper, UserMapper


class UserRepositoryImp(AlchemyRepositoryBase[models.User, dto.UserCreate, dto.User, dto.UserUpdate], UserRepository):
    def __init__(self, session: AsyncSession, mapper: ModelMapper = UserMapper()) -> None:
        super().__init__(session, mapper)

    async def get_by_id(self, user_id: int) -> dto.User | None:
        user = await self._session.get(models.User, user_id)

        return self._mapper.to_repr(user) if user else None

    async def get_by_username(self, username: str) -> dto.User | None:
        user = await self._session.scalar(select(models.User).filter_by(username=username))

        return self._mapper.to_repr(user) if user else None

    async def update(self, user_id: int, user: dto.UserUpdate) -> dto.User | None:
        user_to_update = await self._session.get(models.User, user_id)
        if not user_to_update:
            return None

        self._update_model(user_to_update, dto)

        user_repr: dto.User = self._mapper.to_repr(user_to_update)

        return user_repr

    async def delete(self, user_id: int) -> None:
        await self._session.execute(delete(models.User).filter_by(id=user_id))

    async def create(self, user: dto.UserCreate) -> None:
        user_to_create = self._mapper.to_model_create(user)
        self._session.add(user_to_create)
