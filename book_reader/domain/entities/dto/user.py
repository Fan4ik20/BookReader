from dataclasses import dataclass

__all__ = (
    "User",
    "UserUpdate",
    "UserCreate",
)


@dataclass(frozen=True)
class User:
    id: int
    username: str
    hashed_password: str


@dataclass(frozen=True)
class UserCreate:
    username: str
    hashed_password: str


@dataclass(frozen=True)
class UserUpdate:
    username: str | None
    hashed_password: str | None
