from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Type
from fastapi.templating import Jinja2Templates


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
templates = Jinja2Templates(directory='templates')

users_db = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/')
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users_db})


@app.get('/user/{user_id}')
async def all_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users_db[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.post('/user/{username}/{age}')
async def new_user(username: str, age: int) -> User:
    user_id = max(users_db, key=lambda x: int(x.id)).id + 1 if users_db else 1
    user = User(id=user_id, username=username, age=age)
    users_db.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users_db:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def user_del(user_id: int) -> User:
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return user
    raise HTTPException(status_code=404, detail='User was not found')

# uvicorn module_16_5:app
