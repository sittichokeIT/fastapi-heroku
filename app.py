from fastapi import FastAPI
from routes.route_user import user
app = FastAPI()
app.include_router(user)
