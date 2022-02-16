from sqlalchemy.orm import Session
from fastapi_todoapp.schemas import task as task_schema
from fastapi_todoapp.models.task import Task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, id: int):
    return db.query(Task).filter(Task.id == id).first()

def update_task(db: Session, id: int, task_update: task_schema.TaskUpdate):
    task = db.query(Task).filter(Task.id == id).first()
    task.title = task_update.title
    task.status = task_update.status
    db.commit()
    db.flush()
    return task

def create_task(db: Session, task_create: task_schema.TaskCreate):
    task = Task(title=task_create.title, status=task_create.status)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, id: int) -> None:
    db.query(Task).filter(Task.id == id).delete()
    db.commit()