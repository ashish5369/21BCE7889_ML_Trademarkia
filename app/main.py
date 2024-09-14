from fastapi import FastAPI  
from app.database import engine  
from app.models import Base  
from app.routes import search, health  
from background_tasks import scrape_articles  
import asyncio  

app = FastAPI()  

@app.on_event("startup")  
async def startup():  
    async with engine.begin() as conn:  
        await conn.run_sync(Base.metadata.create_all)  
    asyncio.create_task(scrape_articles())  

app.include_router(search.router)  
app.include_router(health.router)