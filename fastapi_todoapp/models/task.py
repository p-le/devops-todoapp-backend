from sqlalchemy import Boolean, Integer, Column, String, DateTime

from fastapi_todoapp.libs.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)