import pytest

from src.s3 import download

pytestmark = pytest.mark.asyncio

test_email = "example@gmail.com"
save_as = "bossFile.txt"
filepath_to_download = "/mnt/c/Users/tanapon/Downloads/downloadtxt.txt"
filepath_to_download = "C:\\Users\\tanapon\\Downloads\\downloadtxt2.txt"


async def test_download_file():
    resp = await download.download_file(test_email, save_as, filepath_to_download)
    print(resp)
    return resp
    # add your assertions here to verify that the upload_file function works as expected
