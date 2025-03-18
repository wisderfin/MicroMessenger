from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import with_session
from models.auth import JWTRefreshModel, UserModel


@with_session
async def create_jwt_refresh(user_uuid: str, tokens: str, session: AsyncSession) -> None:
    jwt = JWTRefreshModel(user_uuid=user_uuid, refresh_tokens=tokens)
    session.add(jwt)
    await session.commit()

@with_session
async def get_jwt_refresh(user_uuid: str, session: AsyncSession) -> list:
    users = await session.execute(
        select(UserModel)
        .options(joinedload(UserModel.refresh_tokens))
        .filter_by(uuid=user_uuid)
    )
    user = users.scalars().first()

    if user:
        return [token.refresh_tokens for token in user.refresh_tokens]
    return []
