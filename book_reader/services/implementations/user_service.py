from domain.entities import dto
from domain.repositories.interfaces import UserRepository
from services.interfaces import UserService

from .base import ServiceBase
from services import exc


class UserServiceImp(ServiceBase[UserRepository], UserService):
    async def get_by_id(self, user_id: int) -> dto.User:
        user = await self._repo.get_by_id(user_id)

        if not user:
            raise exc.UserNotFound

        return user

    async def get_by_username(self, username: str) -> dto.User:
        user = await self._repo.get_by_username(username)

        if not user:
            raise exc.UserNotFound

        return user

    async def create(self, user: dto.UserCreate) -> dto.User:
        if await self._repo.get_by_username(user.username):
            raise exc.UserWithUsernameAlreadyExist

        async with self._uow:
            new_user = await self._repo.create(user)

        return new_user

    async def update(self, user_id: int, user: dto.UserUpdate) -> dto.User:
        if await self._repo.get_by_username(user.username):
            raise exc.UserWithUsernameAlreadyExist

        async with self._uow:
            updated_user = await self._repo.update(user_id, user)

        return updated_user

    async def delete(self, user_id: int) -> None:
        user = await self._repo.get_by_id(user_id)

        if not user:
            raise exc.UserNotFound

        async with self._uow:
            await self._repo.delete(user_id)
