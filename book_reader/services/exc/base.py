__all__ = ("NotFoundReader", "AlreadyExistReader")


class ReaderError(Exception):
    pass


class NotFoundReader(ReaderError):
    model: str


class AlreadyExistReader(ReaderError):
    model: str
    field: str
