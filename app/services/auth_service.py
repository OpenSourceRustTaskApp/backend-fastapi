from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from datetime import timedelta
from app.core.config import settings
from app.core.security import verify_password, create_access_token
from app.repositories.user_repository import UserRepository
from app.models.user import UserLoginHistory


class AuthService:
    @staticmethod
    async def authenticate_user(db: AsyncSession, email: str, password: str):
        """
        ユーザーを認証し、認証成功時にアクセストークンを生成します。

        :param db: データベースセッション
        :param email: ユーザーのメールアドレス
        :param password: ユーザーのパスワード
        :return: アクセストークンとトークンタイプを含む辞書
        :raises HTTPException: 認証失敗時に発生
        """
        user = await UserRepository.get_user_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="メールアドレスまたはパスワードが正しくありません",
                headers={"WWW-Authenticate": "Bearer"},
            )

        latest_password = await UserRepository.get_latest_password(db, user.user_id)
        if not latest_password or not verify_password(password, latest_password.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="メールアドレスまたはパスワードが正しくありません",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

        # ログイン履歴を記録
        login_history = UserLoginHistory(user_id=user.user_id)
        db.add(login_history)
        await db.commit()

        return {"access_token": access_token, "token_type": "bearer"}
