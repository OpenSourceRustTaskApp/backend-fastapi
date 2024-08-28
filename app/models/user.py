from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Boolean
from sqlalchemy.sql import func
from app.db.database import Base


class User(Base):
    __tablename__ = "m_users"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(20), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    updated_by = Column(BigInteger, nullable=True)
    is_deleted = Column(Boolean, default=False)


class UserEmail(Base):
    __tablename__ = "t_user_emails"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, index=True)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    updated_by = Column(BigInteger, nullable=True)
    is_deleted = Column(Boolean, default=False)


class UserLoginHistory(Base):
    __tablename__ = "t_user_login_histories"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, index=True)
    login_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class UserPassword(Base):
    __tablename__ = "t_user_passwords"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, index=True)
    password = Column(String(255), nullable=False)
    is_latest = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    updated_by = Column(BigInteger, nullable=True)
    is_deleted = Column(Boolean, default=False)
