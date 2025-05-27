from app.infraestructure.repositories.user_repo import DynamoUserRepository
from app.core.usecases.user_service import UserService
from app.services.auth import hash_password, verify_password
from app.services.jwt import create_access_token


def get_user_service() -> UserService:
    return UserService(
        repo=DynamoUserRepository(),
        hasher=hash_password,
        token_creator=create_access_token,
    )
