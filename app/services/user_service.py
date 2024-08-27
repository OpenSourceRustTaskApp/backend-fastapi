from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
        return await UserRepository.get_users(db, skip, limit)
