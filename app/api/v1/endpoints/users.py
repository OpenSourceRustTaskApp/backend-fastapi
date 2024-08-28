from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.user_service import UserService
from app.schemas.user import User, UserCreate
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
    users = await UserService.get_users(db, skip=skip, limit=limit)
    return users


@router.post(
    "/users",
    response_model=User,
    summary="ユーザー登録",
    description="新しいユーザーを登録します。",
    response_description="登録されたユーザーオブジェクト",
)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await UserService.create_user(db, user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
