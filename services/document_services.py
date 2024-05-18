from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List
from domain.models import DocumentEntity,OutletEntity
from services.outlet_services import OutletEntity
from base.bases import DocumentBase
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

def add_document(document:DocumentBase):
    db = next(get_db())
    db_doc = DocumentEntity(**document.dict())
    db.add(db_doc)
    db.commit()

def add_documentList(documents:List[DocumentBase]):
    db = next(get_db())
    for document_data in documents:
        db_doc = DocumentEntity(**document_data.dict())
        db.add(db_doc)
    db.commit()

def find_docements(start_date,end_date,branch):
    db = next(get_db())
    
    # Query database to get documents within the date range
    documents = db.query(DocumentEntity)
    if start_date is not None:
        documents = documents.filter(DocumentEntity.date >= start_date)
    if end_date is not None:
        documents = documents.filter(DocumentEntity.date <= end_date)
    if branch != None:
        documents = documents.filter(DocumentEntity.date <= end_date)
    documents = documents.all()
    return documents
    return doc

def find_document_by_date(start_date:datetime.date=None,end_date:datetime.date=None):
    db = next(get_db())
    # Query database to get documents within the date range
    documents = db.query(DocumentEntity)
    if start_date is not None:
        documents = documents.filter(DocumentEntity.date >= start_date)
    if end_date is not None:
        documents = documents.filter(DocumentEntity.date <= end_date)
    documents = documents.all()
    return documents

def find_document_by_branch(branch_id:int):
    db = next(get_db())
    # Query database to get documents within the date range
    documents = db.query(DocumentEntity)
    documents = documents.filter(DocumentEntity.outlet_id ==branch_id)
    documents = documents.all()
    return documents

def del_doc(doc_id:int):
    db = next(get_db())
    doc = db.query(DocumentEntity).filter(DocumentEntity.id == doc_id).first()
    if doc == None:
        return False
    db.delete(doc)
    db.commit()
    return True