from domain.entities import dto, models

from .base import ModelMapper

__all__ = ("UserMapper",)


class UserMapper(ModelMapper[models.User, dto.UserCreate, dto.User]):
    def to_repr(self, model: models.User) -> dto.User:
        return dto.User(id=model.id, username=model.username, hashed_password=model.hashed_password)

    def to_model_create(self, dto_create: dto.UserCreate) -> models.User:
        return models.User(username=dto_create.username, hashed_password=dto_create.hashed_password)
