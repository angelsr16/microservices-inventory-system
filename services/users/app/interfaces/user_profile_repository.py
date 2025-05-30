from abc import ABC, abstractmethod
from typing import Optional

from core.entities.user_profile import UserProfile


class IUserProfileRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[UserProfile]:
        pass

    @abstractmethod
    def save(self, user_profile: UserProfile) -> None:
        pass
