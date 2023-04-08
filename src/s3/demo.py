from minio import Minio
import urllib3
# import ssl
# print(ssl.OPENSSL_VERSION)

#print url lib3 version
# print(urllib3.util.ssl_.DEFAULT_SSL_CIPHERS)
#
# from urllib3.util.ssl_ import DEFAULT_SSL_CIPHERS
# print(DEFAULT_SSL_CIPHERS)
#Create client

client = Minio(endpoint="tanpantz.com:9000",
               access_key="K41A9jEtlfz413O8",
               secret_key="jhHYonvPuwWNKxERFEoM5G1tzaaYt8d0",
               secure=False)

print("Total buckets:", len(client.list_buckets()))

found = client.bucket_exists("my-bucket")
if not found:
    client.make_bucket("my-bucket")
else:
    print("Bucket 'my-bucket' already exists")

# Upload '/tmp/my_file.txt' as object name 'my_file.txt' to bucket 'my-bucket'.

result = client.fput_object(
    "my-bucket", "my_file.txt", "/mnt/c/Users/tanapon/Desktop/sometext.txt",
)

print("Created {0} with etag: {1}, version-id: {2}".format(
    result.object_name, result.etag, result.version_id,
))



#
# from minio import Minio
# from minio.commonconfig import VersioningConfig
# from minio.error import S3Error
#
# client = Minio(
#     endpoint="tanpantz.com:9000",
#     access_key="K41A9jEtlfz413O8",
#     secret_key="jhHYonvPuwWNKxERFEoM5G1tzaaYt8d0",
#     secure=False
# )
#
# print("Total buckets:", len(client.list_buckets()))
#
# bucket_name = "my-bucket"
# found = client.bucket_exists(bucket_name)
# if not found:
#     client.make_bucket(bucket_name)
# else:
#     print(f"Bucket '{bucket_name}' already exists")
#
# # Enable versioning for the bucket
# config = VersioningConfig(VersioningConfig.ENABLED)
# client.set_bucket_versioning(bucket_name, config)
#
# # Upload the file to the bucket
# result = client.fput_object(
#     bucket_name, "my_file.txt", "/mnt/c/Users/tanapon/Desktop/sometext.txt",
# )
#
# print("Created {0} with etag: {1}, version-id: {2}".format(
#     result.object_name, result.etag, result.version_id,
# ))