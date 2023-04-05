from datetime import datetime
from typing import Dict

from fastapi import Depends
from minio import Minio
from pydantic import EmailStr

from src.s3.service import convert_email_to_bucket
from src.s3.config import minio_config

# from config import minio_config
# from src.auth import service
# from src.auth.jwt import parse_jwt_user_data
# from src.auth.schemas import JWTData, UserResponse

# from src import s3

# client = Minio(endpoint="tanpantz.com:9000",
#                access_key="K41A9jEtlfz413O8",
#                secret_key="jhHYonvPuwWNKxERFEoM5G1tzaaYt8d0",
#                secure=False)

client = Minio(endpoint=minio_config["endpoint"],
               access_key=minio_config["access_key"],
               secret_key=minio_config["secret_key"],
               secure=minio_config["secure"])

print("Total buckets:", len(client.list_buckets()))


async def upload_file(email: EmailStr, save_as: any, filepath_to_upload: any) -> dict[str, str]:
    bucket_name = convert_email_to_bucket(email)
    print("bucket_name: {1}", bucket_name)
    """
    Upload a file to minio storage.

    :param the file that needs to be uploaded
    :return the url that the file can be located at
    """
    try:
        print("trying to upload")
        found = client.bucket_exists(bucket_name)
        if not found:
            client.make_bucket(bucket_name)
        else:
            print("Bucket {0} already exists".format(bucket_name))

        # Upload '/tmp/my_file.txt' as object name 'my_file.txt' to bucket 'email'.
        # result = client.fput_object(
        #     email, "my_file.txt", "/mnt/c/Users/tanapon/Desktop/sometext.txt",
        # )

        result = client.fput_object(
            bucket_name, save_as, filepath_to_upload,
        )
        print("after result")
        print("Created {0} with etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ))

        return {"message": "File uploaded successfully Uploaded!"}

        # {"message": "File uploaded successfully Created {0} with etag: {1}, version-id: {2}".format(
        #     result.object_name, result.etag, result.version_id,
        # )}
        # return get_public_s3_url(filename)
    except Exception as e:
        return {"error": str(e)}

#
# def get_public_s3_url(filename: str, bucket: str) -> str:
#     return f"{s3_config['endpoint_url']}/{bucket}/{filename}"
