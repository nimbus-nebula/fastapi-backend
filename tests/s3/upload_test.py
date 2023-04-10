import os
import platform
from pathlib import Path

import pytest

from src.s3 import upload

pytestmark = pytest.mark.asyncio

test_email = "boss.teh@student.ac.th"
save_as = "bossFile3.txt"
filepath_to_upload = "/mnt/c/Users/tanapon/Desktop/sometext.txt"


@pytest.mark.asyncio
async def test_upload_file():
    bytes_arr = open(filepath_to_upload, "rb")
    resp = await upload.upload_file(test_email, save_as, bytes_arr)
    print(resp)
    bytes_arr.close()
    return resp
    # add your assertions here to verify that the upload_file function works as expected
