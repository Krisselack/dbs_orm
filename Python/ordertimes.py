class Ordertimes:
    __tablename__='ordertimes'
    id=Column()
    orderdate=Column('orderdate',datetime)
    qtr_id=Column('qtr_id',int)
    month_id=Column('month_id',int)
    year_id=Column('year_id',int)