from pydantic import BaseModel
from datetime import datetime

class DocumentBase(BaseModel):
    doc_no:str
    date:datetime
    hour:int
    outlet_id:int

class PostBase(BaseModel):
    doc_id:int
    item_code:str
    item_desc:str
    qty:int
    uom:str
    unit_price:float
    unit_cost:float
    actual_cost:float
    sub_total:float
    unit_profit:float
    issold:bool

class OutletBase(BaseModel):
    outlet_name:str

class UserBase(BaseModel):
    user_name:str
    password:str
    access_grade:int

class AccessBase(BaseModel):
    access_qty:int
    access:str
