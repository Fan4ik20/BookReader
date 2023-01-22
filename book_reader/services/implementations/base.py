from typing import Generic, TypeVar

from domain.repositories.uow import UOW

__all__ = ("ServiceBase",)

Repository = TypeVar("Repository")


class ServiceBase(Generic[Repository]):
    def __init__(self, repo: Repository, uow: UOW) -> None:
        self._repo = repo
        self._uow = uow
