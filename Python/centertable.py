class Centertable:
    __tablename__='ordertimes'
    pk=Column(Integer, primary_key=True)
    on_id = Column(Integer, surrogat_key=True)
    pr_id = Column(Integer,surrogat_key=True)
    cu_id = Column(Integer,surrogat_key=True)
    ordernumber=Column('ordernumber',int)
    quantityorderd=Column('quantityorderd',int)
    priceeach=Column('priceeach',int)
    orderlinenumber=Column('orderlinenumber',int)
    sales = Column('sales', int)
    status = Column('status', str)
    dealsize = Column('dealsize', str)