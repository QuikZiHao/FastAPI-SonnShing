from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List
from domain.models import AccessEntity
from base.bases import AccessBase
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

def add_access(access:AccessEntity):
    db = next(get_db())
    db_access = AccessEntity(**access.dict())
    db.add(db_access)
    db.commit()

def get_access(access_name:str):
    db = next(get_db())
    access = db.query(AccessEntity).filter(AccessEntity.access_name == access_name).first()
    if access_name == None:
        return None
    accessBlock = access.__dict__()
    accessBlock['access'] = access.access.split('\n')
    if len(accessBlock['access'] == access.access_qty):
        return accessBlock
    return None

def del_access(access_id:int):
    db = next(get_db())
    access = db.query(AccessEntity).filter(AccessEntity.id == access_id).first()
    if access == None:
        return False
    db.delete(access)
    db.commit()
    return True