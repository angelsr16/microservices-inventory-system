from typing import List
from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    password: str
    firstName: str
    lastName: str
    roles: List[str]


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
