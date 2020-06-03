class Customertable:
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