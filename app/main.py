import logging
from time import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.v1.endpoints import users, auth
from app.db.database import create_tables
from app.utils.logger import CustomFormatter  # カスタムフォーマッタをインポート

# ロギングの設定
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# SQLAlchemyのログレベルを設定
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

# SQLAlchemyのログフォーマットを変更
formatter = CustomFormatter()
for logger_name in ["sqlalchemy.engine"]:
    sqlalchemy_logger = logging.getLogger(logger_name)
    sqlalchemy_logger.setLevel(logging.INFO)
    sqlalchemy_handler = logging.StreamHandler()
    sqlalchemy_handler.setFormatter(formatter)
    sqlalchemy_logger.addHandler(sqlalchemy_handler)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 起動時の処理
    await create_tables()
    yield
    # シャットダウン時の処理（必要な場合）


app = FastAPI(lifespan=lifespan)

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # フロントエンドのURLを指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# リクエストロギングミドルウェア
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    logger.info(
        f"Request: {request.method} {request.url} - Status: {response.status_code} - Process Time: {process_time:.2f}s"
    )
    return response


app.include_router(users.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")


@app.get("/")
async def root():
    logger.info("Root endpoint was called")
    return {"message": "Welcome to the API"}
