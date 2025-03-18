from datetime import datetime, timedelta, timezone
from jwt import encode, decode

from domain.repositories.user import get_user
from config import config


async def get_jwt(username: str) -> tuple[str]:
    current_time = datetime.now(timezone.utc)
    access = encode(
        {
            'iss': 'auth',
            'user': username,
            'exp': current_time + timedelta(minutes=config.JWT_ACCESS_EXPIRE)
        },
        config.JWT_ACCESS_KEY,
        config.JWT_ALGORITHM
    )
    refresh = encode(
        {
            'iss': 'auth',
            'user': username,
            'exp': current_time + timedelta(days=config.JWT_REFRESH_EXPIRE)
        },
        config.JWT_REFRESH_KEY,
        config.JWT_ALGORITHM
    )

    return access, refresh
