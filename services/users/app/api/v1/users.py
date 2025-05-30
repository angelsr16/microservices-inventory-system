from fastapi import APIRouter, Depends

from api.dependencies.user_profile_service import get_user_profile_service
from core.usecases.user_profile_service import UserProfileService
from schemas.user_profile_schema import UserProfileRegister

router = APIRouter(prefix="/users")


@router.post("/register")
async def register_user(
    user_profile_data: UserProfileRegister,
    user_profile_service: UserProfileService = Depends(get_user_profile_service),
):
    user_profile = user_profile_service.register(user_profile_data)
    return {"msg": "User registered"}
