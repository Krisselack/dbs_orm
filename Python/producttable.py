class Producttable:
    __tablename__='producttable'
    pr_id = Column('pr_id', String(5), primary_key=True)
    msrp = Column('msrp',int)
    productline = Column('productline',String(20))
    productcode = Column('productcode',String(20))
