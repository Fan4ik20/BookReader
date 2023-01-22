from sqlalchemy import Column, Integer, String

from .base import ReaderBase

__all__ = ("User",)


class User(ReaderBase):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(100), unique=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
