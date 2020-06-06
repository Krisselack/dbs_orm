from sqlalchemy import Table, Column, String, Integer, ForeignKey, DateTime
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

    def create_object(self, newObj):
        self.session.add(newObj)
        self.session.commit()

    def delete_object(self,delobj):
        self.session.delete(delobj)
        self.session.commit()

    #bin mir hier nicht sicher ob das einfach alles updated was geändert wurde hier bsp dazu aus https://www.compose.com/articles/using-postgresql-through-sqlalchemy/:
    # Update
    # doctor_strange.title = "Some2016Film"
    # session.commit()
    def update(self):
        self.session.commit()