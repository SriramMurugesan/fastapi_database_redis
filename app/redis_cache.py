import os
import aioredis
from dotenv import load_dotenv
import json


load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")
redis = aioredis.from_url(REDIS_URL, encoding="utf8", decode_responses=True)

async def get_cache(key: str):
    cached = await redis.get(key)
    if cached:
        return json.loads(cached)
    return None

async def set_cache(key: str, value: dict, expire: int = 10):
    await redis.set(key, json.dumps(value), ex=expire)