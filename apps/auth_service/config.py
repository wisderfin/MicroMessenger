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

    class Config:
        env_file = '.env'
        extra = 'ignore'


config = Config()
