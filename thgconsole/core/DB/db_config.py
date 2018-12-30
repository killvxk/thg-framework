import os
import sys
from sqlalchemy import *
from sqlalchemy.orm import *

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite:///thg.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()