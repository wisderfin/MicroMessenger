from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.auth import UserModel
from schemas.auth import SignUpSchema
from schemas.response import ResponseSchema
from infrastructure.database import with_session
from services.password import hash_password


@with_session
async def get_user(username: str, session: AsyncSession) -> UserModel:
    response = await session.execute(select(UserModel).filter_by(username=username))
    user = response.scalar_one_or_none()
    return user


@with_session
async def create_user(data: SignUpSchema, session: AsyncSession) -> ResponseSchema:
    if await get_user(data.username):
        return ResponseSchema(code=409, message=f'User {data.username} already exists')
    data.password = hash_password(data.password)
    user = UserModel(**data.model_dump())
    session.add(user)
    await session.commit()
    return ResponseSchema(code=200, message=f'User {data.username} successfully created')
