from fastapi import APIRouter, Response

from schemas.auth import SignUpSchema, LogInSchema, JWTAccessSchema
from schemas.response import ResponseSchema
from domain.repositories.user import get_user, create_user
from domain.services.coockie import set_tokens


router = APIRouter(prefix="/api/auth", tags=['auth'])


@router.post('/signup')
async def signup(data: SignUpSchema) -> ResponseSchema:
    response = await create_user(data)
    return response


@router.post('/login')
async def signup(
    response: Response,
    data: LogInSchema
) -> JWTAccessSchema:
    user = await get_user(data.username)
    jwt_access = await set_tokens(response, user)
    return JWTAccessSchema(jwt_access=jwt_access)
