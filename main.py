from fastapi import FastAPI,HTTPException,Depends,status,Query
from typing import List
#sql table
import domain.models as models
from base.bases import *
#sql services
from controller.document_controller import router as document_router
from controller.outlet_controller import router as outlet_router
from controller.access_controller import router as access_router
from controller.user_controller import router as user_router
#sql connect
from database import engine,SessionLocal
from sqlalchemy.orm import Session
import uvicorn
import sys
sys.path.append(r"C:\Users\quikz\Desktop\FastAPI SonnShing")

app = FastAPI()
models.Base.metadata.create_all(bind=engine)



# Include routers
app.include_router(document_router, prefix="", tags=["Document"])
app.include_router(outlet_router, prefix="", tags=["Outlet"])
app.include_router(access_router, prefix="", tags=["Access"])
app.include_router(user_router, prefix="", tags=["User"])

if __name__ == '__main__':
    uvicorn.run(app="main:app",reload=True)




