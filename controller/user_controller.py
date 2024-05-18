from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List,Optional
from domain.models import UserEntity
from base.bases import UserBase
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


@router.post('/user/',status_code= status.HTTP_201_CREATED)
async def create_user(user:UserBase):
    userServices.add_user(user=user)

@router.get('/user/{username}',status_code=status.HTTP_200_OK)
async def get_users(userName:str):
    user = userServices.find_user_by_name(userName)
    if user == None:
        raise HTTPException(status_code=404,detail='user not found')
    return user


@router.delete('/user/{user_id}',status_code=status.HTTP_200_OK)
async def delete_users(user_id:int):
    flag = userServices.delete_users(user_id)
    if not flag:
        raise HTTPException(user_code=404,detail='user not found')