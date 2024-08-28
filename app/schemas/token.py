from pydantic import BaseModel


class Token(BaseModel):
    """
    アクセストークンのレスポンスモデル
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    トークンに含まれるデータのモデル
    """

    email: str | None = None


class LoginRequest(BaseModel):
    """
    ログインリクエストのモデル
    """

    email: str
    password: str
