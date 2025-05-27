from fastapi import APIRouter, HTTPException
from app.infraestructure.repositories.user_repo import DynamoUserRepository
from app.schemas.user_schema import UserRegister, UserLogin, TokenResponse
from app.core.usecases.user_service import UserService
from app.services.auth import hash_password, verify_password
from app.services.jwt import create_access_token

router = APIRouter()

user_service = UserService(
    repo=DynamoUserRepository(),
    hasher=hash_password,
    token_creator=create_access_token,
)


@router.post("/register", response_model=TokenResponse)
def register(user_data: UserRegister):
    try:
        token = user_service.register(
            username=user_data.username,
            password=user_data.password,
        )
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(user_data: UserLogin):
    try:
        token = user_service.login(
            username=user_data.username,
            password=user_data.password,
            verifier=verify_password,
        )
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
