from datetime import datetime
from fastapi import Depends
from minio import Minio
from pydantic import EmailStr

from src.s3.service import convert_email_to_bucket
from src.s3.config import minio_config
# from src.s3 import client
# from config import minio_config
# from src.auth import service
# from src.auth.jwt import parse_jwt_user_data
# from src.auth.schemas import JWTData, UserResponse

import os
from pathlib import Path

download_path = str(Path.home() / "Downloads")

print(f"Download path: {download_path}")

client = Minio(endpoint=minio_config["endpoint"],
               access_key=minio_config["access_key"],
               secret_key=minio_config["secret_key"],
               secure=minio_config["secure"])

"""
   Download a file from minio storage.

   :param email, the file that needs to be uploaded, download location
   :return the url that the file can be located at
"""


async def download_file(email: EmailStr, object_name: any, filepath_to_download: any) -> dict[str, str]:
    bucket_name = convert_email_to_bucket(email)
    try:
        found = client.bucket_exists(bucket_name)
        if not found:
            raise Exception(f"Bucket {bucket_name} does not exist")

        result = client.fget_object(
            bucket_name, object_name, filepath_to_download,
        )
        print("Downloaded {0} with etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ))
        return {"message": "File successfully downloaded!"}

    except Exception as e:
        return {"error": str(e)}
