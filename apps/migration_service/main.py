import asyncio
from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from config import config

DATABASE_URL = (
    f"{config.DATABASE_DRIVER}://"
    f"{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@"
    f"{config.DATABASE_HOST}:{config.DATABASE_PORT}/"
    f"{config.DATABASE_NAME}"
)

engine = create_async_engine(DATABASE_URL, echo=False, future=True)


async def run_migrations():
    async with engine.connect() as connection:
        from migrations.env import target_metadata
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if __name__ == "__main__":
    asyncio.run(run_migrations())
