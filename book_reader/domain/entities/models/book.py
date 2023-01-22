from typing import TYPE_CHECKING
from uuid import UUID as TUUID
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import ReaderBase

if TYPE_CHECKING:
    from .user import User


__all__ = ("BookFile",)


class BookFile(ReaderBase):
    __tablename__ = "book_files"

    id: TUUID = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    title: str = Column(String(100), nullable=False)
    author: str | None = Column(String(100))

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user: User = relationship(User, backref="books")
