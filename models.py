# models.py
from sqlalchemy import Column, Integer, String, Text, ARRAY, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(100))
    is_admin = Column(Boolean, default=False)
    documents = relationship("Document", back_populates="owner")

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(Text)
    embeddings = Column(ARRAY(Float))  # For PostgreSQL, this becomes array type
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Make sure this line exists
    owner = relationship("User", back_populates="documents")