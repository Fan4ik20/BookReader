from sqlalchemy.ext.asyncio import AsyncSession

__all__ = ("UOW",)


class UOW:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def __aenter__(self) -> "UOW":
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self._session.rollback()
        else:
            await self._session.commit()

    async def commit(self) -> None:
        await self._session.commit()
