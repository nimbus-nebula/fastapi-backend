from fastapi import APIRouter, Depends, File, UploadFile, Form
from pydantic import EmailStr
from starlette import status
from src.s3 import objects_list
from src.auth import service
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import JWTData
from src.s3.schemas import UploadData
from src.s3 import upload as s3upload
import ast
from io import BytesIO

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(
        file: UploadFile = File(...),
        name: str = Form(...),
        jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> dict[str, str]:
    user = await service.get_user_by_id(jwt_data.user_id)
    file_contents = await file.read()
    file_bytes = BytesIO(file_contents)
    email: EmailStr = user["email"]
    upload_result = await s3upload.upload_file(email, name, file_bytes)
    return upload_result

"""
List files endpoint
"""
@router.get("/list", status_code=status.HTTP_200_OK)
async def list_files(
        jwt_data: JWTData = Depends(parse_jwt_user_data),
):
    user = await service.get_user_by_id(jwt_data.user_id)
    email: EmailStr = user["email"]
    file_lists = await objects_list.list_objects(email)
    literal = ast.literal_eval(file_lists)
    return literal

