from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User


class UserRepository:
    @staticmethod
    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
        query = select(User).offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
