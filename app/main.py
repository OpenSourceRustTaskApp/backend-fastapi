from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.endpoints import users
from app.db.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 起動時の処理
    await create_tables()
    yield
    # シャットダウン時の処理（必要な場合）


app = FastAPI(lifespan=lifespan)

app.include_router(users.router, prefix="/api/v1")
