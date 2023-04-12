from io import BytesIO
import pytest
from async_asgi_testclient import TestClient
from fastapi import status


# @pytest.mark.asyncio
# async def test_upload(client: TestClient):
#     response = await client.post(
#         "/auth/register",
#         json={
#             "email": "fake@test.com",
#             "password": "123Aa!",
#         },
#     )

#     login = await client.post(
#         "/auth/login",
#             json={
#                 "email": "fake@test.com",
#                 "password": "123Aa!",
#             },
#     )
#     login_json = login.json()
#     refresh_token = login_json["refresh_token"]
#     auth_token = login_json["access_token"]

#     fake_file = b"some file data"
#     file_bytes = BytesIO(fake_file)
#     response = await client.post(
#         "/s3/upload",
#         data={"name": "test.txt", "file": (file_bytes, "test.txt")},
#         headers={"Authorization": f"Bearer {auth_token}",
#                  "Cookie": f"refresh_token={refresh_token}"},
#     )
#     assert response.status_code == status.HTTP_201_CREATED
