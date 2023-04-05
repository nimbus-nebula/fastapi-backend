from databases.interfaces import Record
from fastapi import APIRouter, Depends
from pydantic import EmailStr
from starlette import status
from src.s3 import service as s3_service
from src.auth import service
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import UserResponse, JWTData
from src.s3.schemas import UploadData, DownloadData
from src.s3 import upload as s3upload
from src.s3 import download as s3download

router = APIRouter()
@router.get("/dd")
async def say_dd():
    return {"message": f"Hello dd"}

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(
        # payload: dict[str, str],
        upload_data: UploadData,
        jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> dict[str, str]:
    print("hi upload")
    user = await service.get_user_by_id(jwt_data.user_id)
    email: EmailStr = user["email"]
    save_as = upload_data.save_as
    print("save as: ", save_as)
    file_path = upload_data.filepath_to_upload
    print("file_path: ", file_path)
    upload_result = await s3upload.upload_file(email, save_as, file_path)
    print(upload_result)
    # print("hi upload3: {0}".format(upload_result))
    return {
        upload_result
        # "message": "File uploaded successfully",  # type: ignore
    }

@router.get("/download", )
async def download_file(
    download_data: DownloadData,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
):
    user = await service.get_user_by_id(jwt_data.user_id)
    email: EmailStr = user["email"]
    download_result = await s3download.download_file(email, download_data.obj_name, download_data.filepath_to_download)
    return {download_result}

@router.post("/message", status_code=status.HTTP_201_CREATED)
async def post_message(
        payload: dict[str, str],
        jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> dict[str, str]:
    post = await service.send_message(payload, jwt_data.user_id)
    return post

"""
List files endpoint
"""
@router.get("/list", )
async def list_files(
        jwt_data: JWTData = Depends(parse_jwt_user_data),

):
    user = await service.get_user_by_id(jwt_data.user_id)
    email: EmailStr = user["email"]
    file_lists = await s3download.download_file(email)
    return {file_lists}



# @router.post("/create/bucket")
# async def create_bucket():
#     # TODO: Create a new bucket in s3
#     return {"message": "Bucket created successfully"}
