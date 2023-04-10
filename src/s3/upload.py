from minio import Minio
from pydantic import EmailStr

from src.s3.config import minio_config
from src.s3.service import convert_email_to_bucket

client = Minio(
    endpoint=minio_config["endpoint"],
    access_key=minio_config["access_key"],
    secret_key=minio_config["secret_key"],
    secure=minio_config["secure"],
)


async def upload_file(email: EmailStr, save_as: any, filebytes: any) -> dict[str, str]:
    bucket_name = convert_email_to_bucket(email)
    print("bucket_name: {0}".format(bucket_name))
    """
    Upload a file to minio storage.

    :param the file that needs to be uploaded
    :return the url that the file can be located at
    """
    try:
        print("trying to upload")
        found = client.bucket_exists(bucket_name)
        if not found:
            print("Attempting to make bucket")
            client.make_bucket(bucket_name)
        else:
            print("Bucket {0} already exists".format(bucket_name))
            result = client.put_object(
                bucket_name,
                save_as,
                filebytes,
                -1,
                part_size=10 * 1024 * 1024,
            )
        print("after result")
        print(
            "Created {0} with etag: {1}, version-id: {2}".format(
                result.object_name,
                result.etag,
                result.version_id,
            )
        )

        return {"message": "File uploaded successfully Uploaded!"}

    except Exception as e:
        return {"error": str(e)}
