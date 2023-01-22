from domain.entities import dto, models

from .base import ModelMapper

__all__ = ("BookFileMapper",)


class BookFileMapper(ModelMapper[models.BookFile, dto.BookFileCreate, dto.BookFile]):
    def to_repr(self, model: models.BookFile) -> dto.BookFile:
        return dto.BookFile(id=model.id, title=model.title, author=model.author, user_id=model.user_id)

    def to_model_create(self, dto_create: dto.BookFileCreate) -> models.BookFile:
        return models.BookFile(title=dto_create.title, author=dto_create.author, user_id=dto_create.user_id)
