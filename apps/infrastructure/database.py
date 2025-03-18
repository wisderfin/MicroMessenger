from functools import wraps
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import Any, AsyncGenerator, Callable, Coroutine, TypeVar

from config import config


engine = create_async_engine(
    f"{config.DATABASE_DRIVER}://"
    f"{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@"
    f"{config.DATABASE_HOST}:{config.DATABASE_PORT}/"
    f"{config.DATABASE_NAME}"
)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


# генератор сессия базы данных
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


T = TypeVar("T", bound=Callable[..., Coroutine[Any, Any, Any]])  # for save annotations


def with_session(func: T) -> T:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        session: AsyncSession = kwargs.get("session")
        if session is None:
            async with async_session_maker() as session:
                kwargs["session"] = session
                return await func(*args, **kwargs)
        else:
            return await func(*args, **kwargs)

    return wrapper
