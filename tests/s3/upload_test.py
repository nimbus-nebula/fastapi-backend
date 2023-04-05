import pytest
from src.s3 import upload
import os
from pathlib import Path
import platform

pytestmark = pytest.mark.asyncio

test_email = "example@gmail.com"
save_as = "bossFile2.txt"
filepath_to_upload = "/mnt/c/Users/tanapon/Desktop/sometext.txt"

async def test_upload_file():
    resp = await upload.upload_file(test_email, save_as, filepath_to_upload)
    print(resp)
    return resp
    # add your assertions here to verify that the upload_file function works as expected

def test_downloadpath():
    # client_os = 'Windows' #platform.system()
    # if client_os == 'Windows':
    #     download_path = str(Path.home() / "Downloads")
    # elif client_os == 'Darwin':
    #     download_path = str(Path.home() / "Downloads")
    # else:
    #     download_path = str(Path.home() / "Downloads")
    # print(f"Download path: {download_path}")

    folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'folder_name')
    print(folder)
    return