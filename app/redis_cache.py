import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_cache(key: str):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None

def set_cache(key: str, value, expire: int = 60):
    r.set(key, json.dumps(value), ex=expire)
