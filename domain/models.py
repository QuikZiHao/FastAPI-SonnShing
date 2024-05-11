from sqlalchemy import Boolean,Column,Integer,String,Date,Float
from database import Base

class DocumentEntity(Base):
    __tablename__ = 'Doc'

    id = Column(Integer,primary_key=True,index=True)
    doc_no = Column(String(12))
    date = Column(Date)
    hour = Column(Integer)
    outlet_id = Column(Integer)

class PostEntity(Base):
    __tablename__ = 'post'

    id = Column(Integer,primary_key=True,index=True)
    doc_id = Column(Integer)
    item_code = Column(String(50))
    item_desc = Column(String(50))
    qty = Column(Float)
    uom = Column(String(20))
    unit_price = Column(Float)
    unit_cost = Column(Float)
    actual_cost = Column(Float)
    sub_total = Column(Float)
    unit_profit = Column(Float)
    issold = Column(Boolean)

class OutletEntity(Base):
    __tablename__ = 'outlet'

    id = Column(Integer,primary_key=True,index=True)
    outlet_name = Column(String(50))

class UserEntity(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String(20),unique=True)
    password = Column(String(20))
    access_grade = Column(Integer)

class AccessEntity(Base):
    __tablename__ = 'access'

    id = Column(Integer,primary_key=True,index=True)
    access_qty = Column(Integer)
    access = Column(String(100))

