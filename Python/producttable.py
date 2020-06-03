class Producttable:
    __tablename__='producttable'
    on_id = Column('on_id', String(32), primary_key=True)
    orderdate = Column('orderdate',datetime)
    qtr_id = Column('qtr_id',int)
    month_id = Column('month_id',int)
    year_id = Column('year_id',int)