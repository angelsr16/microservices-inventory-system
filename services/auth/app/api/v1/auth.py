from fastapi import APIRouter, Depends, HTTPException
from api.dependencies.user_service import get_user_service
from schemas.user_schema import UserRegister, UserLogin, TokenResponse
from core.usecases.user_service import UserService
from services.auth import hash_password, verify_password

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
def register(
    user_data: UserRegister, user_service: UserService = Depends(get_user_service)
):
    try:
        token = user_service.register(user_data)
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(user_data: UserLogin, user_service: UserService = Depends(get_user_service)):
    try:
        token = user_service.login(
            username=user_data.username,
            password=user_data.password,
        )
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
