from .base import NotFoundReader


__all__ = ("BookFileNotFound",)


class BookFileNotFound(NotFoundReader):
    model: str = "BookFile"
