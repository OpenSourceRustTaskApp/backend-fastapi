import os
from pydantic_settings import BaseSettings
from datetime import timedelta


class Settings(BaseSettings):
    DATABASE_URL: str = (
        f"mysql+aiomysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@db/{os.getenv('MYSQL_DATABASE')}"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()

if not settings.SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in the .env file")
