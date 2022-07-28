from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user  = APIRouter()

Path = conn.HEROKU.user

@user.post('/create')
async def create(user: User):
    Path.insert_one(dict(user))
    return {
        "message":"Added user to the database"
    }

@user.get('/show')
async def show():
    return {
        "result": usersEntity(Path.find())
    }

