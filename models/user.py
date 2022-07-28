from pydantic import BaseModel

class User(BaseModel):
    Id: str
    name: str
    email: str
    password: str
