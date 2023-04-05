import re

from pydantic import EmailStr, Field, validator

from src.auth.schemas import STRONG_PASSWORD_PATTERN
from src.models import ORJSONModel


class AuthUser(ORJSONModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)

    @validator("password")
    def valid_password(cls, password: str) -> str:
        if not re.match(STRONG_PASSWORD_PATTERN, password):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password


class UploadData(ORJSONModel):
    save_as: str
    filepath_to_upload: str

class DownloadData(ORJSONModel):
    obj_name: str
    filepath_to_download: str

# class JWTData(ORJSONModel):
#     user_id: int = Field(alias="sub")
#     is_admin: bool = False
#
#
# class AccessTokenResponse(ORJSONModel):
#     access_token: str
#     refresh_token: str
#
#
# class UserResponse(ORJSONModel):
#     email: EmailStr
