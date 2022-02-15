from sqlalchemy import Boolean, Integer, Column, String, DateTime
from sqlalchemy.sql import func

from fastapi_todoapp.libs.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())