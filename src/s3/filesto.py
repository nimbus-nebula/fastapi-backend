import os
from datetime import datetime

import boto3

from src.s3.config import s3_config

s3 = boto3.resource(**s3_config)


def upload_file(file: any) -> str:
    """
    Upload a file to minio storage.

    :param the file that needs to be uploaded
    :return the url that the file can be located at
    """

    try:
        # TODO: Need to find a more dynamic way to retrieve the bucket
        bucket = os.environ.get("S3_BUCKET")
        timestamp = datetime.utcnow().isoformat()
        filetype = file.filename.split(".")[-1]
        filename = f"{timestamp}{filetype}"

        s3.Bucket(bucket).Object(filename).put(Body=file.read())

        return get_public_s3_url(filename)
    except Exception as e:
        return {"error": str(e)}


def get_public_s3_url(filename: str, bucket: str) -> str:
    return f"{s3_config['endpoint_url']}/{bucket}/{filename}"
