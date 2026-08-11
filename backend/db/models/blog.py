from db.base_class import Base
from sqlalchemy import Column, String, Boolean, Integer, DECIMAL, DateTime, Text, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Blog(Base):
    id = Column(Integer, primary_key=True)