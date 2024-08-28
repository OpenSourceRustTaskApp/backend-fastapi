from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User, UserEmail, UserPassword


class UserRepository:
    @staticmethod
    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
        """
        指定された範囲のユーザーを取得します。

        :param db: データベースセッション
        :param skip: スキップするユーザー数（デフォルト: 0）
        :param limit: 取得するユーザーの最大数（デフォルト: 100）
        :return: 取得されたユーザーのリスト
        """
        query = select(User).offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str):
        """
        指定されたメールアドレスに対応するユーザーを取得します。

        :param db: データベースセッション
        :param email: 検索するユーザーのメールアドレス
        :return: UserEmailオブジェクト。ユーザーが見つからない場合はNone
        """
        query = select(UserEmail).where(UserEmail.email == email)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @staticmethod
    async def get_latest_password(db: AsyncSession, user_id: int):
        """
        指定されたユーザーIDに対応する最新のパスワードを取得します。

        :param db: データベースセッション
        :param user_id: ユーザーID
        :return: 最新のUserPasswordオブジェクト。存在しない場合はNone
        """
        query = (
            select(UserPassword)
            .where(UserPassword.user_id == user_id, UserPassword.is_latest == True)
            .order_by(UserPassword.created_at.desc())
        )
        result = await db.execute(query)
        return result.scalar_one_or_none()
