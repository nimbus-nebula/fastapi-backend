from databases.interfaces import Record
from fastapi import APIRouter
from src.auth import jwt, service, utils
from src.auth.dependencies import (
    valid_refresh_token,
    valid_refresh_token_user,
    valid_user_create,
)
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import AccessTokenResponse, AuthUser, JWTData, UserResponse

router = APIRouter()

@router.post("/upload",)
async def upload_file():
    # TODO: Upload file endpoint
    return {"message": "File uploaded successfully"}

@router.get("/download",)
async def download_file():
    # TODO: Download file endpoint
    return {"message": "File downloaded successfully"}

@router.get("/list",)
async def list_files():
    # TODO: List files endpoint
    return {"message": "Files listed successfully"}
