from minio import Minio

from src.s3.config import minio_config

client = Minio(
    endpoint=minio_config["endpoint"],
    access_key=minio_config["access_key"],
    secret_key=minio_config["secret_key"],
    secure=minio_config["secure"],
)
