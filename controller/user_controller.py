from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List,Optional
from domain.models import DocumentEntity
from base.bases import DocumentBase
from database import SessionLocal
from sqlalchemy.orm import Session
import services.user_services as userServices
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




@router.post('/doc/',status_code=status.HTTP_202_CREATED)
async def create_user(user:UserBase):
    userServices.add_user(user=user)

@router.post('/docList/',status_code=status.HTTP_202_CREATED)
async def create_users_list(users:List[userBase]):
    userServices.add_userList(users=users)

@router.get('/doc/{doc_id}',status_code=status.HTTP_200_OK)
async def get_users(doc_id:int):
    user = userServices.find_users_by_id(doc_id)
    if user == None:
        raise HTTPException(status_code=404,detail='user not found')
    return user

@router.get('/doc/date/', status_code=status.HTTP_200_OK)
async def get_users_date(start_date: Optional[str] = None , end_date: Optional[str] = None):
    try:
        # Convert date strings to datetime objects
        start_date_obj = None if start_date is None else datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = None if end_date is None else datetime.strptime(end_date, '%Y-%m-%d').date()

        # Query database to get documents within the date range
        users = userServices.find_user_by_date(start_date=start_date_obj,end_date=end_date_obj)
        # Check if documents exist for the given date range
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return {"users":users}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Dates must be in YYYY-MM-DD format.")

# need to add check the branch valid or not
@router.get('/doc/branch/', status_code=status.HTTP_200_OK)
async def get_users_branch(branch_id:int):
    """
    branchList = getBrachList
    if branch_id not in branchList:
        raise HTTPException(user_code=400, detail="Branch Not Found.")
    """
    users = userServices.find_document_by_branch(branch_id=branch_id)
    # Check if documents exist for the given date range
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return {"users":users}


@router.delete('/doc/{doc_id}',status_code=status.HTTP_200_OK)
async def delete_users(doc_id:int):
    flag = userServices.del_doc(doc_id)
    if not flag:
        raise HTTPException(user_code=404,detail='doc not found')