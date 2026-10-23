import redis.asyncio as redis
from app.core.config import settings

redis_client: redis.Redis | None = None


async def get_redis() -> redis.Redis:
    """Get or initialize Redis client."""
    global redis_client
    if redis_client is None:
        redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)
    return redis_client


async def check_idempotency(delivery_id: str, ttl_seconds: int = 86400) -> bool:
    """Check if webhook delivery ID was already processed.

    Returns True if delivery is new and successfully recorded, False if already seen.
    """
    client = await get_redis()
    key = f"hetupr:delivery:{delivery_id}"
    is_new = await client.set(key, "processed", ex=ttl_seconds, nx=True)
    return bool(is_new)
