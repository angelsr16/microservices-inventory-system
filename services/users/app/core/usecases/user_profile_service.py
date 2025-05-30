from datetime import datetime, timezone
from core.entities.user_profile import UserProfile
from interfaces.user_profile_repository import IUserProfileRepository
from schemas.user_profile_schema import UserProfileRegister


class UserProfileService:
    def __init__(self, repo: IUserProfileRepository):
        self.repo = repo

    def register(self, user_profile_register: UserProfileRegister):
        now_utc = datetime.now(timezone.utc)

        user_profile = UserProfile(
            username=user_profile_register.username,
            firstName=user_profile_register.firstName,
            lastName=user_profile_register.lastName,
            roles=user_profile_register.roles,
            created_at=now_utc,
            updated_at=now_utc,
        )

        self.repo.save(user_profile=user_profile)
        return user_profile
