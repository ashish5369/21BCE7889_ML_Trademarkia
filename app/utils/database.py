from fastapi import FastAPI, Depends  
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  
from sqlalchemy.orm import sessionmaker  
from sqlalchemy.ext.declarative import declarative_base  

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"  # Update with your actual database URL  
engine = create_async_engine(DATABASE_URL, echo=True)  
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)  
Base = declarative_base()  

app = FastAPI()  

async def get_db() -> AsyncSession:  
    async with AsyncSessionLocal() as session:  
        yield session  

@app.on_event("startup")  
async def startup():  
    async with engine.begin() as conn:  
        await conn.run_sync(Base.metadata.create_all)  

@app.get("/items/")  
async def read_items(db: AsyncSession = Depends(get_db)):  
    # Your database query logic here  
    pass