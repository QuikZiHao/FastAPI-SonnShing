from fastapi import APIRouter, HTTPException, Depends, Query,status
from typing import List,Optional
from domain.models import DocumentEntity
from base.bases import DocumentBase
from database import SessionLocal
from sqlalchemy.orm import Session
import services.document_services as documentServices
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




@router.post('/doc/',status_code=status.HTTP_201_CREATED)
async def create_documents(document:DocumentBase):
    documentServices.add_document(document=document)

@router.post('/docList/',status_code=status.HTTP_201_CREATED)
async def create_documents_list(documents:List[DocumentBase]):
    documentServices.add_documentList(documents=documents)

@router.get('/doc/',status_code=status.HTTP_200_OK)
async def get_documents(start_date: Optional[str] = None , end_date: Optional[str] = None , branch: Optional[str] = None):
    try:
        # Convert date strings to datetime objects
        start_date_obj = None if start_date is None else datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = None if end_date is None else datetime.strptime(end_date, '%Y-%m-%d').date()
        doc = documentServices.find_docements(start_date=start_date_obj,end_date=end_date_obj,branch)
        if doc == None:
            raise HTTPException(status_code=404, detail="No documents found")
        return doc
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Dates must be in YYYY-MM-DD format.")
    

@router.get('/doc/date/', status_code=status.HTTP_200_OK)
async def get_documents_date(start_date: Optional[str] = None , end_date: Optional[str] = None , branch: Optional[str] = None):
    try:
        # Convert date strings to datetime objects
        start_date_obj = None if start_date is None else datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = None if end_date is None else datetime.strptime(end_date, '%Y-%m-%d').date()

        # Query database to get documents within the date range
        documents = documentServices.find_document_by_date(start_date=start_date_obj,end_date=end_date_obj)
        # Check if documents exist for the given date range
        if not documents:
            raise HTTPException(status_code=404, detail="No documents found")
        return {"documents":documents}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Dates must be in YYYY-MM-DD format.")

# need to add check the branch valid or not
@router.get('/doc/branch/', status_code=status.HTTP_200_OK)
async def get_documents_branch(branch_id:int):
    """
    branchList = getBrachList
    if branch_id not in branchList:
        raise HTTPException(status_code=400, detail="Branch Not Found.")
    """
    documents = documentServices.find_document_by_branch(branch_id=branch_id)
    # Check if documents exist for the given date range
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found")
    return {"documents":documents}


@router.delete('/doc/{doc_id}',status_code=status.HTTP_200_OK)
async def delete_documents(doc_id:int):
    flag = documentServices.del_doc(doc_id)
    if not flag:
        raise HTTPException(status_code=404,detail='doc not found')
