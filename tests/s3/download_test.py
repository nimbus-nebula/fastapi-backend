import pytest
from src.s3 import download

pytestmark = pytest.mark.asyncio

test_email = "example@gmail.com"
save_as = "bossFile.txt"
filepath_to_upload = "/home/tanapon/Downloads"
async def test_download_file():
    resp = await download.download_file(test_email, save_as, filepath_to_upload)
    print(resp)
    return resp
    # add your assertions here to verify that the upload_file function works as expected