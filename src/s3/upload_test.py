import asyncio

import pytest

from src.s3 import upload

test_email: str = "example@gmail.com"
save_as: any = "bossFile.txt"
filepath_to_upload: any = "/mnt/c/Users/tanapon/Desktop/sometext.txt"

# @pytest.fixture
async def testing(test_email, save_as, filepath_to_upload):
    print("before the fn called")
    resp = await upload.upload_file(test_email, save_as, filepath_to_upload)
    return


print("hi")
asyncio.run(testing(test_email, save_as, filepath_to_upload))
print("done")
