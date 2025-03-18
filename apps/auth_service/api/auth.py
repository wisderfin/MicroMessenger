from fastapi import APIRouter

from schemas.auth import SignUpSchema
from schemas.response import ResponseSchema
from domain.repositories.user import create_user


router = APIRouter(prefix="/api/auth", tags=['auth'])


@router.post('/signup')
async def signup(data: SignUpSchema) -> ResponseSchema:
    response = await create_user(data)
    return response
