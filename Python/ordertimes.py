from sqlalchemy import Table, Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

class Ordertimes:
    __tablename__='ordertimes'
    on_id = Column('on_id', String(5),primary_key=True)
    orderdate = Column('orderdate',datetime)
    qtr_id = Column('qtr_id',int)
    month_id = Column('month_id',int)
    year_id = Column('year_id',int)
    centertable = relationship('Centertable', back_populates='ordertimes')

    def __init__(self, orderdate, qtr_id, month_id, year_id, centertable):
        self.orderdate = orderdate
        self.qtr_id = qtr_id
        self.month_id = month_id
        self.year_id = year_id
        self.centertable = centertable