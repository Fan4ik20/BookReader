from typing import Protocol

from domain.entities import dto

__all__ = ("UserRepository",)


class UserRepository(Protocol):
    async def get_by_id(self, user_id: int) -> dto.User | None:
        raise NotImplementedError

    async def get_by_username(self, username: str) -> dto.User | None:
        raise NotImplementedError

    async def update(self, user_id: int, user: dto.UserUpdate) -> dto.User | None:
        raise NotImplementedError

    async def delete(self, user_id: int) -> None:
        raise NotImplementedError

    async def create(self, user: dto.UserCreate) -> None:
        raise NotImplementedError
