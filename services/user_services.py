from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List
from domain.models import UserEntity,AccessEntity
from base.bases import UserBase
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

def add_user(user:UserEntity):
    db = next(get_db())
    db_user = UserEntity(**user.dict())
    db.add(db_user)
    db.commit()

def find_user_by_name(user_name:str):
    db = next(get_db())
    query = (
        db.query(UserEntity, AccessEntity)
        .outerjoin(AccessEntity, UserEntity.access_grade == AccessEntity.id)
        .filter(UserEntity.user_name == user_name)
        .first()
    )
    if query == None:
        return None
    user,access = query
    output = {
        "user_id": user.id,
        "user_name": user.user_name,
        "password": user.password,
        "access_qty" : access.access_qty,
        "access" : access.access.split(';')
    }
    if len(output['access']) == output["access_qty"]: 
        return output
    return None 


def del_user(user_id:int):
    db = next(get_db())
    user = db.query(UserEntity).filter(UserEntity.id == user_id).first()
    if user == None:
        return False
    db.delete(user)
    db.commit()
    return True