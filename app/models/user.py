from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.sql import func
from app.db.database import Base


class User(Base):
    __tablename__ = "m_users"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(20), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    updated_by = Column(BigInteger)
    is_deleted = Column(Integer, default=0)
