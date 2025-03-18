from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DATABASE_DRIVER: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str

    AUTH_PORT: int

    BCRYPT_ROUNDS: int

    JWT_ALGORITHM: str
    JWT_ACCESS_EXPIRE: int
    JWT_ACCESS_KEY: str
    JWT_REFRESH_EXPIRE: int
    JWT_REFRESH_KEY: str

    COOKIE_JWT_REFRESH_KEY: str
    COOKIE_JWT_ACCESS_KEY: str

    class Config:
        env_file = '.env'
        extra = 'ignore'


config = Config()
