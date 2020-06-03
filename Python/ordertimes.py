class Ordertimes:
    __tablename__='ordertimes'
    on_id = Column('on_id', String(5),primary_key=True)
    orderdate = Column('orderdate',datetime)
    qtr_id = Column('qtr_id',int)
    month_id = Column('month_id',int)
    year_id = Column('year_id',int)
    centertable = relationship('Centertable', uselist=False, back_populates='ordertimes')