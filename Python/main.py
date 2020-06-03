
# import packages

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import classes
from Python.centertable import Centertable
# from Python.customertable import Customertable

# create an engine
engine = create_engine('postgresql://usr:pass@localhost:5432/postgres')

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()
session
