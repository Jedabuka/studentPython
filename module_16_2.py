from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get("/")
async def main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_page_id(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=69)):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_page(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter User ID",
                                                  example="Djon")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=88)]):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


# uvicorn module_16_2:app
