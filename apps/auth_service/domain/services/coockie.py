from fastapi import Response, Request

from config import config
from models.auth import UserModel
from domain.repositories.jwt import create_jwt_refresh
from domain.services.jwt import get_jwt


async def get_coockie(request: Request) -> tuple[str, str]:
    access = request.cookies.get(config.COOKIE_JWT_ACCESS_KEY)
    refresh = request.cookies.get(config.COOKIE_JWT_REFRESH_KEY)
    return access, refresh


async def set_refresh_coockie(
        response: Response,
        value: str
) -> None:
    response.delete_cookie(config.COOKIE_JWT_REFRESH_KEY)
    response.set_cookie(
        key=config.COOKIE_JWT_REFRESH_KEY,
        value=value,
        httponly=True,
        max_age=config.JWT_REFRESH_EXPIRE * 24 * 60 * 60,
        secure=True,
        samesite='lax'
    )


async def set_access_cookie(
        responce: Response,
        value: str
) -> None:
    responce.delete_cookie(config.COOKIE_JWT_ACCESS_KEY)
    responce.set_cookie(
        key=config.COOKIE_JWT_ACCESS_KEY,
        value=value,
        httponly=False,
        max_age=config.JWT_ACCESS_EXPIRE * 60,
        secure=True,
        samesite='lax'
    )


async def set_tokens(
        response: Response,
        user_model: UserModel
) -> str:
    access, refresh = await get_jwt(user_model.username)
    await create_jwt_refresh(user_model.uuid, refresh)
    await set_refresh_coockie(response, refresh)
    await set_access_cookie(response, access)
    return access
