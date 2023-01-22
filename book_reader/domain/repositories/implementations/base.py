from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from domain.mappers import ModelMapper

Model = TypeVar("Model")
DTO = TypeVar("DTO")
DTOCreate = TypeVar("DTOCreate")
DTOUpdate = TypeVar("DTOUpdate")

__all__ = ("AlchemyRepositoryBase",)


class AlchemyRepositoryBase(Generic[Model, DTOCreate, DTO, DTOUpdate]):
    def __init__(self, session: AsyncSession, mapper: ModelMapper) -> None:
        self._session = session
        self._mapper = mapper

    @staticmethod
    def _update_model(model: Model, dto: DTOUpdate) -> Model:
        for attr, value in vars(dto).items():
            if attr and value and hasattr(model, attr):
                setattr(model, attr, value)

        return model

    async def commit(self) -> None:
        await self._session.commit()
