from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

# 日本標準時（JST）のタイムゾーンを設定
JST = timezone(timedelta(hours=9))

# パスワードハッシュ化のためのコンテキストを設定
# bcryptスキームを使用し、非推奨のスキームは自動的に処理
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    プレーンテキストのパスワードとハッシュ化されたパスワードを比較検証します。

    :param plain_password: ユーザーが入力したプレーンテキストのパスワード
    :param hashed_password: データベースに保存されているハッシュ化されたパスワード
    :return: パスワードが一致する場合はTrue、それ以外はFalse
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    与えられたパスワードをハッシュ化します。

    :param password: ハッシュ化するプレーンテキストのパスワード
    :return: ハッシュ化されたパスワード
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    JWTアクセストークンを生成します。

    :param data: トークンに含めるデータ（通常はユーザー識別情報）
    :param expires_delta: トークンの有効期限（省略可能）
    :return: 生成されたJWTトークン
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(JST) + expires_delta
    else:
        expire = datetime.now(JST) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
