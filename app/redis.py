import aioredis  

REDIS_URL = "redis://localhost:6379"  

async def get_redis():  
    return await aioredis.from_url(REDIS_URL)