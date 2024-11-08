from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def all_users() -> dict:
    return users_db

@app.post('/user/{username}/{age}')
async def new_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                 example='UrbanUser')]
                   , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='20')]) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    users_db[current_index] = username, age
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(ge=1, le=200, description='Enter User ID', example=111)],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='20')]) -> str:
    users_db[user_id] = username, age
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def user_del(user_id: Annotated[str, Path(ge=1, le=200, description='Enter User ID', example=111)]) -> str:
    users_db.pop(user_id)
    return f'User {user_id} has been deleted'


# uvicorn module_16_3:app


