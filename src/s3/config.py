import os

from dotenv import load_dotenv

load_dotenv()


s3_user = os.environ.get("S3_USER")
s3_password = os.environ.get("S3_PASSWORD")
s3_host = os.environ.get("S3_HOST")
s3_port = os.environ.get("S3_PORT")
s3_access_key = os.environ.get("S3_ACCESS_KEY")
s3_secret_key = os.environ.get("S3_SECRET_KEY")
print(s3_user)

s3_config = {
    "service_name": "s3",
    "aws_access_key_id": s3_user,
    "aws_secret_access_key": s3_password,
    "endpoint_url": f"http://{s3_host}:{s3_port}",
    "verify": False,
}

minio_config = {
    "endpoint": f"{s3_host}:{s3_port}",
    "access_key": s3_access_key,
    "secret_key": s3_secret_key,
    "secure": False,
}
print(minio_config["endpoint"], minio_config["access_key"])
# client = Minio(endpoint="tanpantz.com:9000",
#                access_key="K41A9jEtlfz413O8",
#                secret_key="jhHYonvPuwWNKxERFEoM5G1tzaaYt8d0",
#                secure=False)
