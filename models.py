# app/models.py

from sqlalchemy import Column, String, Boolean, Text, Integer, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class BagScan(Base):
    __tablename__ = "bag_scans"
    
    id = Column(Integer, primary_key=True, index=True)
    bag_tag_id = Column(String(50), index=True)
    destination_gate = Column(String(50))
    location_scanned = Column(String(100))
    timestamp = Column(DateTime, server_default=func.now())
    
    
    