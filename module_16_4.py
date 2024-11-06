from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import List, Type


app = FastAPI()

users_db = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def all_users() -> List[User]:
    return users_db


@app.post('/user/{username}/{age}')
async def new_user(username: str, age: int) -> User:
    add_user = User(id=len(users_db) + 1, username=username, age=age)
    users_db.append(add_user)
    return add_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        users_db[user_id - 1] = User(id=user_id, username=username, age=age)
        return users_db[user_id - 1]

    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def user_del(user_id: int) -> User:
    if user_id == users_db[user_id - 1].id:
        return users_db.pop(user_id - 1)
    else:
        raise HTTPException(status_code=404, detail='User was not found')


# uvicorn module_16_4:app
