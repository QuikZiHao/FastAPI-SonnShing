from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List,Optional
from domain.models import AccessEntity
from base.bases import AccessBase
from database import SessionLocal
from sqlalchemy.orm import Session
import services.access_services as accessServices
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

@router.post('/access/',status_code=status.HTTP_201_CREATED)
async def create_outlets(access:AccessBase):
    accessServices.add_access(access=access)

@router.get('/access/{access_name}',status_code=status.HTTP_200_OK)
async def get_access(access_name:str):
    access = accessServices.get_access(access_name==access_name)
    if access == None:
        raise HTTPException(status_code=404,detail='access not found')
    return access


@router.delete('/access/{access_id}',status_code=status.HTTP_200_OK)
async def delete_access(access_id:int):
    flag = accessServices.del_access(access_id=access_id)
    if not flag:
        raise HTTPException(status_code=404,detail='access not found')
