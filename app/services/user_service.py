from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.models.user import User, UserEmail, UserPassword

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    @staticmethod
    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
        return await UserRepository.get_users(db, skip, limit)

    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate):
        async with db.begin():
            try:
                # メールアドレスの重複チェック
                existing_user = await UserRepository.get_user_by_email(db, user.email)
                if existing_user:
                    raise HTTPException(status_code=400, detail="Email already registered")

                hashed_password = pwd_context.hash(user.password)

                # ユーザー作成
                db_user = User(username=user.username)
                db.add(db_user)
                await db.flush()

                # メールアドレス登録
                db_email = UserEmail(user_id=db_user.id, email=user.email)
                db.add(db_email)

                # パスワード登録
                db_password = UserPassword(user_id=db_user.id, password=hashed_password)
                db.add(db_password)

                await db.flush()
                await db.refresh(db_user)

                return db_user
            except IntegrityError as e:
                await db.rollback()
                raise HTTPException(status_code=400, detail="Database integrity error. User might already exist.")
            except Exception as e:
                await db.rollback()
                raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
