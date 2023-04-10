from __future__ import annotations

from datetime import timedelta
from typing import Optional, Union

from aioredis import Redis

from src.models import ORJSONModel

redis_client: Redis = None  # type: ignore


class RedisData(ORJSONModel):
    key: Union[bytes, str]
    value: Union[bytes, str]
    ttl: Optional[Union[int, timedelta]]


async def set_redis_key(redis_data: RedisData, *, is_transaction: bool = False) -> None:
    async with redis_client.pipeline(transaction=is_transaction) as pipe:
        await pipe.set(redis_data.key, redis_data.value)
        if redis_data.ttl:
            await pipe.expire(redis_data.key, redis_data.ttl)

        await pipe.execute()


async def get_by_key(key: str) -> Optional[str]:
    return await redis_client.get(key)


async def delete_by_key(key: str) -> None:
    return await redis_client.delete(key)
