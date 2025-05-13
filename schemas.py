# app/schemas.py

from pydantic import BaseModel, EmailStr
from datetime import datetime

class BagScanCreate(BaseModel):
    bag_tag_id: str
    destination_gate: str
    location_scanned: str
    
class BagScanOut(BagScanCreate):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True

