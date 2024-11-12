from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User, Task
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The user was not found')


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], new_user: CreateUser):
    user = db.scalar(select(User).where(User.username == new_user.username))
    if user:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail='Sorry, User already exists')

    else:
        db.execute(insert(User).values(username=new_user.username, firstname=new_user.firstname,
                                       lastname=new_user.lastname, age=new_user.age, slug=slugify(new_user.username)))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, change_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user:
        db.execute(update(User).where(User.id == user_id).values(firstname=change_user.firstname,
                                                                 lastname=change_user.lastname, age=change_user.age))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The user was not found')


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    del_user = db.scalar(select(User).where(User.id == user_id))
    if del_user:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The user was not found')
