# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
import models, schemas, crud
from typing import List


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.post("/baggage/scan", response_model=schemas.BagScanOut)
async def add_bag_scan(scan: schemas.BagScanCreate, db: AsyncSession):
    return await crud.create_bag_scan(db, scan)

@app.get("/baggage/scans/bag/{bag_tag_id}", response_model=List[schemas.BagScanOut])
async def get_scans_for_bag(bag_tag_id: str, latest: bool = False, db: AsyncSession = Depends(get_db)):
    if latest:
        scan = crud.get_latest_scan(db, bag_tag_id)
        if not scan:
            raise HTTPException(status_code=404)
        return scan
    return crud.get_scans_by_bag_tag(db, bag_tag_id)

@app.get("/baggage/scans/gate/{destination_gate}", response_model=list[schemas.BagScanOut])
async def get_scans_for_gate(destination_gate: str, db: AsyncSession = Depends(get_db)):
    return await crud.get_scan_by_gate(db, destination_gate)
