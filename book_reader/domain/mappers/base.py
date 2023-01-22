from typing import Iterable, Protocol, TypeVar

Model = TypeVar("Model")
DTO = TypeVar("DTO")
DTOCreate = TypeVar("DTOCreate")
DTOUpdate = TypeVar("DTOUpdate")


__all__ = ("ModelMapper",)


class ModelMapper(Protocol[Model, DTOCreate, DTO]):
    def to_repr_list(self, models: Iterable[Model]) -> list[DTO]:
        return [self.to_repr(model) for model in models]

    def to_repr(self, model: Model) -> DTO:
        raise NotImplementedError

    def to_model_create(self, dto_create: DTOCreate) -> Model:
        raise NotImplementedError
