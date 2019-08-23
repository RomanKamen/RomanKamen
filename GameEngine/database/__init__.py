from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DB_PATH

engine = create_engine(DB_PATH)
Base = declarative_base()

from .models import *

Session = sessionmaker(engine)
session = Session()

