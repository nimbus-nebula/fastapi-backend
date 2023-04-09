import re

from pydantic import EmailStr, Field, validator, BaseModel

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
    file: any

