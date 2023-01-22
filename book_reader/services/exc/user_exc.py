from .base import NotFoundReader, AlreadyExistReader


__all__ = ("UserNotFound", "UserWithUsernameAlreadyExist",)


class UserNotFound(NotFoundReader):
    model: str = "User"


class UserWithUsernameAlreadyExist(AlreadyExistReader):
    model: str = "User"
    field: str = "username"
