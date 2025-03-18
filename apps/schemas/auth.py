import re

from pydantic import field_validator
from schemas.base import BaseSchema


class BaseAuthSchema(BaseSchema):
    pass


class SignUpSchema(BaseAuthSchema):
    username: str
    password: str

    @field_validator('username')
    def usename_validator(cls, v: str) -> str:
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError("Username must contain only Latin letters, digits, or underscores")

        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters long")

        if len(v) > 50:
            raise ValueError("Username must not exceed 20 characters")

        return v.lower()

    @field_validator('password')
    def password_validator(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.match(r'^[a-zA-Z0-9!@#$%^&*()_+-=]+$', v):
            raise ValueError("Password must contain only Latin letters, digits, and special characters")

        if not re.search(r'[a-zA-Z]', v):
            raise ValueError("Password must contain at least one letter")

        if not re.search(r'[0-9]', v):
            raise ValueError("Password must contain at least one digit")

        if not re.search(r'[!@#$%^&*()_+-=]', v):
            raise ValueError("Password must contain at least one special character")

        return v


class LogInSchema(BaseAuthSchema):
    username: str
    password: str


class BaseJWTSchema(BaseSchema):
    pass


class JWTAccessSchema(BaseJWTSchema):
    jwt_access: str
    type: str = 'bearer'
