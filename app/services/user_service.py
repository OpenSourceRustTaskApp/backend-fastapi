from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return UserRepository.get_users(db, skip, limit)
