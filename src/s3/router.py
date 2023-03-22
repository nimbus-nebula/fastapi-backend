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
    # File1: https://s3.amazonaws.com/bucket-name/file1
    # File2: https://s3.amazonaws.com/bucket-name/file2

    #return [(File1, url...), (File2, url...)]
    
    return {"message": "Files listed successfully"}

@router.post("/create/bucket")
async def create_bucket():
    # TODO: Create a new bucket in s3
    return {"message": "Bucket created successfully"}
