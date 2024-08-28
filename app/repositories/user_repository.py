from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User, UserEmail, UserPassword
from app.schemas.user import UserCreate
from typing import Optional


class UserRepository:
    @staticmethod
    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
        query = select(User).offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate, hashed_password: str, updated_by: Optional[int] = None):
        db_user = User(username=user.username, updated_by=updated_by)
        db.add(db_user)
        await db.flush()

        db_email = UserEmail(user_id=db_user.id, email=user.email)
        db_password = UserPassword(user_id=db_user.id, password=hashed_password)

        db.add(db_email)
        db.add(db_password)
        await db.commit()
        await db.refresh(db_user)

        return db_user
