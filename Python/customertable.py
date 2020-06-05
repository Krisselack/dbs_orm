from sqlalchemy import Table, Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

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