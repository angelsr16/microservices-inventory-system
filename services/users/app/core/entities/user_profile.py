from dataclasses import dataclass
import datetime
from typing import List


@dataclass
class UserProfile:
    username: str
    firstName: str
    lastName: str
    roles: List[str]
    created_at: datetime
    updated_at: datetime
