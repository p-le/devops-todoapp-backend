from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(..., example="running", max_length=1024)
    status: bool = Field(False, description="done task or not")

class Task(TaskBase):
    id: int = Field(..., example=1)
    
    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass