class Ordertimes:
    __tablename__='ordertimes'
    id=Column(Integer,primary_key=True)
    on_id=Column('on_id', String(32))
    orderdate=Column('orderdate',datetime)
    qtr_id=Column('qtr_id',int)
    month_id=Column('month_id',int)
    year_id=Column('year_id',int)