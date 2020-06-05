from sqlalchemy import Column, String, Integer, DateTime  # ',Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Ordertimes(Base):
    __tablename__ = 'ordertimes'
    on_id = Column('on_id', String(5), primary_key=True)
    orderdate = Column('orderdate', DateTime())
    qtr_id = Column('qtr_id', Integer)
    month_id = Column('month_id', Integer)
    year_id = Column('year_id', Integer)
    centertable = relationship('Centertable', back_populates='ordertimes')

    def __init__(self, orderdate, qtr_id, month_id, year_id, centertable):
        self.orderdate = orderdate
        self.qtr_id = qtr_id
        self.month_id = month_id
        self.year_id = year_id
        self.centertable = centertable
