import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI
from routers import task, user

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)


# python -m uvicorn main:app
# python -m app.main runserver
# uvicorn main:app --reload
# uvicorn app.main:app --reload

