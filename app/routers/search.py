from fastapi import APIRouter, Query, HTTPException  
from app.services.search_service import handle_search  
from app.utils.database import SessionLocal  
from app.models.user import User  
import redis  

router = APIRouter()  
redis_client = redis.Redis()  

@router.post("/search")  
async def search(text: str, user_id: str, top_k: int = Query(10), threshold: float = Query(0.5)): 
    db = SessionLocal()  
    user = db.query(User).filter(User.user_id == user_id).first()  
    
    if user is None:  
        user = User(user_id=user_id)  
        db.add(user)  
        db.commit()  
    
    if user.request_count >= 5:  
        raise HTTPException(status_code=429, detail="Too Many Requests")  
    
    user.request_count += 1  
    db.commit()  
    
    results = await handle_search(text, top_k, threshold)  
    return {"results": results}