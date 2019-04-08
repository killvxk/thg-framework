from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db import *
try:
    engine = create_engine('sqlite:///THG.db')
    check = "connect"
except:
    check = "off"
Base.metadata.bind =engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

