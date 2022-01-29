from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(..., example="running", max_length=1024)


class Task(TaskBase):
    id: int = Field(..., example=1)
    status: bool = Field(False, description="done task or not")

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    status: bool = Field(False, description="done task or not")