from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

center_product_association = Table('center_product',  Base.metadata,
    Column('pk', Integer, ForeignKey('centertable.pk')),
    Column('pr_id', Integer, ForeignKey('producttable.pr_id'))
)


class Centertable:
    __tablename__ = 'centertable'
    pk = Column(Integer, primary_key=True)
    on_id = Column(Integer, ForeignKey('ordernumbertable.on_id'))
    pr_id = Column(Integer, ForeignKey('producttable.pr_id'))
    cu_id = Column(Integer, ForeignKey('customertable.cu_id'))
    ordernumber = Column('ordernumber', Integer)
    quantityorderd = Column('quantityorderd', Integer)
    priceeach = Column('priceeach', Integer)
    orderlinenumber = Column('orderlinenumber', Integer)
    sales = Column('sales', Integer)
    status = Column('status', String(50))
    dealsize = Column('dealsize', String(50))
    ordertimes = relationship('Ordertimes', uselist=False, back_populates='ordertimes')
    producttable = relationship("Producttable", secondary=center_product_association)

    def __init__(self, ordernumber, quantityorderd, priceeach,
                 orderlinenumber, sales, status, dealsize):

        self.ordernumber = ordernumber
        self.quantityorderd = quantityorderd
        self.priceeach = priceeach
        self.orderlinenumber = orderlinenumber
        self.sales = sales
        self.status = status
        self.dealsize = dealsize
