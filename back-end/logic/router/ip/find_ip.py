from fastapi import APIRouter, HTTPException
from db.database import db
from db.models import User

router = APIRouter()


@router.get("/ips_unique")
async def get_all_ips():
    all_ips = db.query(User).all()
    return all_ips


