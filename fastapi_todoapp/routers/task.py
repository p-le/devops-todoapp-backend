from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from fastapi_todoapp.schemas import task as task_schema
from fastapi_todoapp.repositories import task as task_respository
from fastapi_todoapp.libs.database import get_db

router = APIRouter(prefix="/tasks", tags=["task"])

@router.get("", response_model=List[task_schema.Task])
async def get_tasks(db: Session=Depends(get_db)):
    return task_respository.get_tasks(db)

@router.get("/{id}", response_model=task_schema.Task)
def get_task(id: int, db: Session=Depends(get_db)):
    task = task_respository.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task

@router.put("/{id}", response_model=task_schema.Task)
def update_task(id: int, task_update: task_schema.TaskUpdate, db: Session=Depends(get_db)):
    task = task_respository.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task_respository.update_task(db, id, task_update)

@router.post("", response_model=task_schema.Task)
def create_task(task_create: task_schema.TaskCreate, db: Session=Depends(get_db)):
    return task_respository.create_task(db, task_create)


@router.delete("/{id}", response_model=task_schema.Task)
def delete_task(id: int, db: Session=Depends(get_db)):
    task = task_respository.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task_respository.delete_task(db, id)