from typing import List
from pydantic import BaseModel


class UserProfileRegister(BaseModel):
    username: str
    firstName: str
    lastName: str
    roles: List[str]