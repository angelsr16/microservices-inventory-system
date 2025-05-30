from fastapi import Depends
from core.usecases.user_profile_service import UserProfileService
from infraestructure.repositories.user_profile_repo import (
    DynamoUserProfileRepository,
)


def get_user_repository():
    return DynamoUserProfileRepository()


def get_user_profile_service(repo=Depends(get_user_repository)):
    return UserProfileService(
        repo=repo,
    )


def create_user_profile_service() -> UserProfileService:
    repo = DynamoUserProfileRepository()
    return UserProfileService(repo)
