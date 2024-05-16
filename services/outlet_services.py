from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List
from domain.models import OutletEntity
from base.bases import OutletBase
from database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime
import time


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_outlet(outlet:OutletEntity):
    db = next(get_db())
    db_outlet = OutletEntity(**outlet.dict())
    db.add(db_outlet)
    db.commit()

def find_outlet_by_name(outlet_name:str):
    db = next(get_db())
    outlet_name = db.query(OutletEntity).filter(OutletEntity.outlet_name == outlet_name).first()
    if outlet_name == None:
        return None
    return outlet_name

def del_outlet(outlet_int:int):
    db = next(get_db())
    outlet = db.query(OutletEntity).filter(OutletEntity.id == outlet_int).first()
    if outlet == None:
        return False
    db.delete(outlet)
    db.commit()
    return True