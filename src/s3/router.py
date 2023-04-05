from databases.interfaces import Record
from fastapi import APIRouter, Depends
from pydantic import EmailStr
from starlette import status
from src.s3 import service as s3_service
from src.auth import service
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import UserResponse, JWTData
from src.s3.schemas import UploadData
from src.s3 import upload as s3Upload

# from minio import Minio

router = APIRouter()


# @router.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
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
    upload_result = await s3Upload.upload_file(email, save_as, file_path)
    print(upload_result)
    # print("hi upload3: {0}".format(upload_result))
    return {
        upload_result
        # "message": "File uploaded successfully",  # type: ignore
    }


@router.post("/message", status_code=status.HTTP_201_CREATED)
async def post_message(
        payload: dict[str, str],
        jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> dict[str, str]:
    post = await service.send_message(payload, jwt_data.user_id)
    return post


@router.get("/download", )
async def download_file():
    # TODO: Download file endpoint
    return {"message": "File downloaded successfully"}


@router.get("/list", )
async def list_files():
    # TODO: List files endpoint
    # File1: https://s3.amazonaws.com/bucket-name/file1
    # File2: https://s3.amazonaws.com/bucket-name/file2

    # return [(File1, url...), (File2, url...)]

    return {"message": "Files listed successfully"}


@router.post("/create/bucket")
async def create_bucket():
    # TODO: Create a new bucket in s3
    return {"message": "Bucket created successfully"}
