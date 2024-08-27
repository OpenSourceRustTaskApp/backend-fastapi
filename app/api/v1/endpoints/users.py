from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import UserService
from app.schemas.user import User
from typing import List

router = APIRouter()


@router.get("/users", response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ユーザー一覧を取得するAPI"""
    users = UserService.get_users(db, skip=skip, limit=limit)
    return users
