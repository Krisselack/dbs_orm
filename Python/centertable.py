from sqlalchemy import Table, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Centertable(Base):
    __tablename__ = 'centertable'
    pk = Column(String(8), primary_key=True)
    on_id = Column(String(5), ForeignKey("ordertimes.on_id"))
    pr_id = Column(String(5), ForeignKey("producttable.pr_id"))
    cu_id = Column(String(5), ForeignKey("customertable.cu_id"))
    ordernumber = Column('ordernumber', Integer)
    quantityordered = Column('quantityordered', Integer)
    priceeach = Column('priceeach', Integer)
    orderlinenumber = Column('orderlinenumber', Integer)
    sales = Column('sales', Integer)
    status = Column('status', String(50))
    dealsize = Column('dealsize', String(50))
    ordertimes = relationship("Ordertimes", back_populates='centertable')
    producttable = relationship("Producttable", back_populates='centertable')
    customertable = relationship("Customertable", back_populates='centertable')

    def __init__(self, ordernumber, quantityorderd, priceeach, orderlinenumber, sales, status, dealsize):
        self.ordernumber = ordernumber
        self.quantityorderd = quantityorderd
        self.priceeach = priceeach
        self.orderlinenumber = orderlinenumber
        self.sales = sales
        self.status = status
        self.dealsize = dealsize

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

class Producttable(Base):
    __tablename__ = 'producttable'
    pr_id = Column('pr_id', String(5), primary_key=True)
    msrp = Column('msrp', Integer)
    productline = Column('productline', String(20))
    productcode = Column('productcode', String(20))
    centertable = relationship('Centertable', back_populates='producttable')

    def __init__(self, msrp, productline, productcode):
        self.msrp = msrp
        self.productline = productline
        self.productcode = productcode

class Customertable(Base):
    __tablename__='customertable'
    cu_id = Column('cu_id', String(5),primary_key=True)
    customername=Column('customername',String(50))
    phone = Column('phone', String(20))
    addressline1 =  Column('addressline1', String(50))
    addressline2 = Column('addressline2', String(50))
    city = Column('city', String(50))
    state = Column('STATE', String(20))
    postalcode = Column('postalcode',String(20))
    country = Column('country', String(20))
    territory = Column('territory',String(20))
    contactlastname = Column('contactlastname', String(20))
    contactfirstname = Column('contactfirstname', String(20))
    centertable = relationship("Centertable", back_populates='customertable')

    def __init__(self,customername,phone,addressline1,addressline2,city,state,postalcode,country,territory,contactlastname,contactfirstname,centertable):
        self.customername = customername
        self.phone = phone
        self.addressline1 = addressline1
        self.addressline2 = addressline2
        self.city = city
        self.state = state
        self.postalcode = postalcode
        self.country = country
        self.territory = territory
        self.contactlastname = contactlastname
        self.contactfirstname = contactfirstname
        self.centertable = centertable