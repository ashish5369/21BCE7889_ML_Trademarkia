from pydantic import BaseModel  

class SearchRequest(BaseModel):  
    text: str  
    top_k: int = 5  
    threshold: float = 0.5  
    user_id: str