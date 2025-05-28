from abc import ABC, abstractmethod
from typing import Optional
from core.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
