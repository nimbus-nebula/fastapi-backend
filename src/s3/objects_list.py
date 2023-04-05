from datetime import datetime
from typing import Dict
from fastapi import Depends
from minio import Minio
from src.s3.service import convert_email_to_bucket
from src.s3.config import minio_config
from datetime import timedelta

client = Minio(endpoint=minio_config["endpoint"],
               access_key=minio_config["access_key"],
               secret_key=minio_config["secret_key"],
               secure=minio_config["secure"])


async def list_objects(email: str) -> [dict[str, list[tuple[str, str]]] | dict[str, str]]:
    bucket_name = convert_email_to_bucket(email)
    try:
        found = client.bucket_exists(bucket_name)
        if not found:
            raise Exception(f"Bucket {bucket_name} does not exist")

        objects = client.list_objects(bucket_name)
        object_names_urls = []
        for obj in objects:
            url = client.get_presigned_url(
                "GET",
                bucket_name,
                obj.object_name,
                expires=timedelta(hours=2),
            )
            object_names_urls.append((obj.object_name, url))
        return {email: object_names_urls}

    except Exception as e:
        return {"error": str(e)}

# async def list_objects(email: str) -> [dict[str, list[str]] | dict[str, str]]:
#
#     bucket_name = convert_email_to_bucket(email)
#     try:
#         found = client.bucket_exists(bucket_name)
#         if not found:
#             raise Exception(f"Bucket {bucket_name} does not exist")
#
#         objects = client.list_objects(bucket_name)
#         object_names = [obj.object_name for obj in objects]
#         url = client.get_presigned_url(
#             "GET",
#             "my-bucket",
#             "my-object",
#             expires=timedelta(hours=2),
#         )
#         return {email: object_names}
#
#     except Exception as e:
#         return {"error": str(e)}
