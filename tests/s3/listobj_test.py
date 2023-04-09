import pytest
from src.s3 import objects_list

pytestmark = pytest.mark.asyncio

test_email = "example@gmail.com"
save_as = "bossFile.txt"
filepath_to_upload = "/mnt/c/Users/tanapon/Downloads/sometext.txt"

@pytest.mark.asyncio
async def test_object_list():
    resp = await  objects_list.list_objects(test_email)
    print(resp)
    return resp
    # add your assertions her