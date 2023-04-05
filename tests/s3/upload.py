import pytest
from async_asgi_testclient import TestClient
from fastapi import status

from src.auth.constants import ErrorCode
from src.s3 import upload

# async def upload_file(email: str, save_as: any, filepath_to_upload: any) -> dict[str, str]:

test_email: str = "example@gmail.com"
save_as: any = "bossFile.txt"
filepath_to_upload: any = "/mnt/c/Users/tanapon/Desktop/sometext.txt"
@pytest.mark.asyncio
async def test_upload(test_email, save_as, filepath_to_upload ) -> None:
    resp = await upload.upload_file(test_email, save_as, filepath_to_upload)
    resp_json = resp.json()

    # assert resp.status_code == status.HTTP_201_CREATED
    # assert resp_json == {"email": "email@fake.com"}

@pytest.mark.asyncio
async def test_register(client: TestClient) -> None:
    resp = await client.post(
        "/auth/users",
        json={
            "email": "email@fake.com",
            "password": "123Aa!",
        },
    )
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_201_CREATED
    assert resp_json == {"email": "email@fake.com"}
