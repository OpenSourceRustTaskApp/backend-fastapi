from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.user_service import UserService
from app.schemas.user import User
from typing import List

router = APIRouter()


@router.get(
    "/users",
    response_model=List[User],
    summary="ユーザー一覧の取得",
    description="登録されているユーザーの一覧を取得します。ページネーションをサポートしています。",
    response_description="ユーザーオブジェクトのリスト",
)
async def get_users(
    skip: int = Query(0, description="スキップするユーザー数", ge=0),
    limit: int = Query(100, description="取得するユーザーの最大数", le=100),
    db: AsyncSession = Depends(get_db),
):
    """
    ユーザー一覧を取得するAPI

    - **skip**: スキップするユーザー数（オプション、デフォルト: 0）
    - **limit**: 取得するユーザーの最大数（オプション、デフォルト: 100）
    """
    users = await UserService.get_users(db, skip=skip, limit=limit)
    return users
