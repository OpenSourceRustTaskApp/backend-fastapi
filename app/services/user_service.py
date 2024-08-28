from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    @staticmethod
    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
        return await UserRepository.get_users(db, skip, limit)

    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate):
        hashed_password = pwd_context.hash(user.password)
        return await UserRepository.create_user(db, user, hashed_password, updated_by=None)
