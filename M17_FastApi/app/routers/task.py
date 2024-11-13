from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        return task
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The task was not found')


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, new_task: CreateTask):
    user = db.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    task = db.scalar(select(Task).where(Task.title == new_task.title))
    if task:
        raise HTTPException(status_code=status.HTTP_306_RESERVED, detail='Sorry, title already exists')

    else:
        db.execute(insert(Task).values(title=new_task.title, content=new_task.content, priority=new_task.priority,
                                       user_id=user_id, slug=slugify(new_task.title)))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, change_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task:
        db.execute(update(Task).where(Task.id == task_id).values(title=change_task.title, content=change_task.content,
                                                                 priority=change_task.priority))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The task was not found')


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    del_task = db.scalar(select(Task).where(Task.id == task_id))
    if del_task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The user was not found')
