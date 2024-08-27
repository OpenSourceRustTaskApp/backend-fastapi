from sqlalchemy import Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "m_users"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(20), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    updated_by = Column(BigInteger)
    is_deleted = Column(Integer, default=0)

    login_histories = relationship("UserLoginHistory", back_populates="user")


class UserLoginHistory(Base):
    __tablename__ = "t_user_login_histories"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("m_users.id"), nullable=False)
    login_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="login_histories")
