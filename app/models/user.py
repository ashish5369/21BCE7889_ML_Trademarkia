from sqlalchemy import Column, Integer, String  
from app.utils.database import Base  

class User(Base):  
    __tablename__ = "users"  

    user_id = Column(String, primary_key=True, index=True)  
    request_count = Column(Integer, default=0)