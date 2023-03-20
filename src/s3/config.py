import os

s3_user = os.environ.get("S3_USER")
s3_password = os.environ.get("S3_PASSWORD")
s3_host = os.environ.get("S3_HOST")
s3_port = os.environ.get("S3_PORT")


s3_config = {
    "service_name": "s3",
    "aws_access_key_id": s3_user,
    "aws_secret_access_key": s3_password,
    "endpoint_url": f"http://{s3_host}:{s3_port}",
    "verify": False,
}
