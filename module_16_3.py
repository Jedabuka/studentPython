from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def all_users() -> dict:
    return users_db

@app.post('/user/{username}/{age}')
async def new_user(username: str, age: int) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    users_db[current_index] = username, age
    return f'User {current_index} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    users_db[user_id] = username, age
    return f'User {user_id} has been updated'

@app.delete('/user/{user_id}')
async def user_del(user_id: str) -> str:
    users_db.pop(user_id)
    return f'User {user_id} has been deleted'


# uvicorn module_16_3:app


