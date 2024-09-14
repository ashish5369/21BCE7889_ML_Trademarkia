from fastapi import FastAPI  
from app.routers import search  
from app.utils.database import Base, engine  

app = FastAPI()  

@app.on_event("startup")  
async def startup():  
    Base.metadata.create_all(bind=engine)  

@app.get("/health")  
async def health_check():  
    return {"status": "API is active"}  

app.include_router(search.router)