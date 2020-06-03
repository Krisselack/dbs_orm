from sqlalchemy import create_engine
# create an engine
engine = create_engine('postgresql://usr:pass@localhost:5432/postgres')

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()