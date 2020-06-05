from sqlalchemy import Table, Column, String, Integer, ForeignKey, Date
# import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# import classes
from centertable import Centertable
from centertable import Customertable
from centertable import Ordertimes
from centertable import Producttable

# create an engine
# postgresql://username:password@host:port/db-name
engine = create_engine('postgresql://postgres:Test@localhost:5432/postgres')

# create a configured "Session" class
Session = sessionmaker(engine)

# create a Session
session = Session()

#just test below
#get all data from Ordertimes in film and print month.id
film = session.query(Ordertimes)
for x in film:
    print(x)

