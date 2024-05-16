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


# need to add check the branch valid or not
@router.get('/doc/branch/', status_code=status.HTTP_200_OK)
async def get_outlets_branch(branch_id:int):
    """
    branchList = getBrachList
    if branch_id not in branchList:
        raise HTTPException(status_code=400, detail="Branch Not Found.")
    """
    outlets = outletservices.find_document_by_branch(branch_id=branch_id)
    # Check if outlets exist for the given date range
    if not outlets:
        raise HTTPException(status_code=404, detail="No outlets found")
    return {"outlets":outlets}


@router.delete('/doc/{doc_id}',status_code=status.HTTP_200_OK)
async def delete_outlets(doc_id:int):
    flag = outletservices.del_doc(doc_id)
    if not flag:
        raise HTTPException(status_code=404,detail='doc not found')
