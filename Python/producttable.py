from sqlalchemy import Column, String, Integer  # ', Table, ForeignKey, Date
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship


class Producttable:
    __tablename__ = 'producttable'
    pr_id = Column('pr_id', String(5), primary_key=True)
    msrp = Column('msrp', Integer)
    productline = Column('productline', String(20))
    productcode = Column('productcode', String(20))

    def __init__(self, msrp, productline, productcode):
        self.msrp = msrp
        self.productline = productline
        self.productcode = productcode
