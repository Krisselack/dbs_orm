center_product_association = Table('center_product', Base.metadata,
    Column('pk', Integer, ForeignKey('centertable.pk')),
    Column('pr_id', Integer, ForeignKey('producttable.pr_id'))
)
class Centertable:
    __tablename__='centertable'
    pk = Column(Integer, primary_key=True)
    on_id = Column(Integer, foreign_key=True)
    pr_id = Column(Integer,foreign_key=True)
    cu_id = Column(Integer,foreign_key=True)
    ordernumber=Column('ordernumber',int)
    quantityorderd=Column('quantityorderd',int)
    priceeach=Column('priceeach',int)
    orderlinenumber=Column('orderlinenumber',int)
    sales = Column('sales', int)
    status = Column('status', str)
    dealsize = Column('dealsize', str)

    ordertimes = relationship('Ordertimes', uselist=False, back_populates='ordertimes')
    cu_id = Column(String(5), ForeignKey('customertable.cu_id'))
    producttable = relationship("Producttable", secondary=center_product_association)