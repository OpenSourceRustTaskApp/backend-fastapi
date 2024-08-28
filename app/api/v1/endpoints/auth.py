from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.auth_service import AuthService
from app.schemas.token import Token
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/login",
    response_model=Token,
    summary="ユーザーログイン",
    description="メールアドレスとパスワードを使用してユーザー認証を行い、アクセストークンを発行します。",
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    """
    ユーザーのログイン処理を行い、アクセストークンを発行します。

    :param form_data: OAuth2PasswordRequestForm（username欄にメールアドレスを使用）
    :param db: データベースセッション
    :return: アクセストークンを含むTokenオブジェクト
    :raises HTTPException: 認証失敗時に発生
    """
    logger.info(f"Login attempt for user: {form_data.username}")
    try:
        token = await AuthService.authenticate_user(db, form_data.username, form_data.password)
        logger.info(f"Login successful for user: {form_data.username}")
        return token
    except HTTPException as e:
        logger.warning(f"Login failed for user: {form_data.username}. Reason: {e.detail}")
        raise
