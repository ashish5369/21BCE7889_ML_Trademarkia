from sqlalchemy import Column, Integer, String  
from sqlalchemy.ext.declarative import declarative_base  

Base = declarative_base()  

class User(Base):  
    __tablename__ = "users"  
    id = Column(Integer, primary_key=True, index=True)  
    user_id = Column(String, unique=True, index=True)  
    request_count = Column(Integer, default=1)