# app/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .models import BagScan
from .schemas import BagScanCreate

async def create_bag_scan(db: AsyncSession, scan: BagScanCreate):
    bag = BagScan(**scan.model_dump())
    await db.add(bag)
    await db.commit()
    await db.refresh(bag)
    return bag

async def get_scans_by_bag_tag(db: AsyncSession, bag_tag_id: str):
    return await db.query(BagScan).filter_by(bag_tag_id=bag_tag_id).order_by(BagScan.timestamp.desc()).all()

async def get_scan_by_gate(db: AsyncSession, destination_gate: str):
    return await db.query(BagScan).filter_by(destination_gate=destination_gate).order_by(BagScan.timestamp.desc()).all()

async def get_latest_scan(db: AsyncSession, bag_tag_id: str):
    return await db.query(BagScan).filter_by(bag_tag_id=bag_tag_id).order_by(BagScan.timestamp.desc()).first()




