from fastapi import APIRouter, Depends
from pydantic import EmailStr
from starlette import status
from src.s3 import objects_list
from src.auth import service
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import JWTData
from src.s3.schemas import UploadData
from src.s3 import upload as s3upload
import ast

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(
        upload_data: UploadData,
        jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> dict[str, str]:
    user = await service.get_user_by_id(jwt_data.user_id)
    email: EmailStr = user["email"]
    save_as = upload_data.save_as
    print("save as: ", save_as)
    file = upload_data.file
    upload_result = await s3upload.upload_file(email, save_as, file)
    print(upload_result)
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

