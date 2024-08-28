from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    updated_by: Optional[int] = None
    is_deleted: bool

    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str
