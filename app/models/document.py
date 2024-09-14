from sqlalchemy import Column, Integer, String  
from app.utils.database import Base  

class Document(Base):  
    __tablename__ = "documents"  

    document_id = Column(Integer, primary_key=True, index=True)  
    content = Column(String)