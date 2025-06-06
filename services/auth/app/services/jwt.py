from datetime import datetime, timedelta
from jose import JWTError, jwt
import core_settings


def create_access_token(data: dict):
    payload = {
        "sub": data["username"],
    }
    return jwt.encode(
        payload, core_settings.JWT_SECRET, algorithm=core_settings.JWT_ALGORITHM
    )
