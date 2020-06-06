from sqlalchemy import Table, Column, String, Integer, ForeignKey, Date
# import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# import classes
from centertable import Centertable
from centertable import Customertable
from centertable import Ordertimes
from centertable import Producttable

class Database():

    def __init__(self,username,password,host,port,dbname):
        # create an engine
        # postgresql://username:password@host:port/db-name
        engine = create_engine('postgresql://'+username+':'+password+'@'+host+':'+str(port)+'/'+dbname)

        # create a configured "Session" class
        Session = sessionmaker(engine)

        # create a Session
        self.session = Session()

    def get_table(self, test):
        return self.session.query(test)