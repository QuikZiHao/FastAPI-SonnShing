from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List,Optional
from domain.models import OutletEntity
from base.bases import OutletBase
from database import SessionLocal
from sqlalchemy.orm import Session
import services.outlet_services as outletServices
from datetime import datetime
import time


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

router = APIRouter()

@router.post('/outlet/',status_code=status.HTTP_201_CREATED)
async def create_outlets(outlet:OutletBase):
    outletServices.add_outlet(outlet=outlet)

@router.get('/outlet/{outlet_name}',status_code=status.HTTP_200_OK)
async def get_outlets(outlet_name:str):
    outlet = outletServices.find_outlet_by_name(outlet_name=outlet_name)
    if outlet == None:
        raise HTTPException(status_code=404,detail='outlet not found')
    return outlet


@router.delete('/outlet/{outlet_id}',status_code=status.HTTP_200_OK)
async def delete_outlets(outlet_id:int):
    flag = outletServices.delete_outlets(outlet_id)
    if not flag:
        raise HTTPException(status_code=404,detail='outlet not found')
