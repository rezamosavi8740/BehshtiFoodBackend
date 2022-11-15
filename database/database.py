from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = "postgresql://postgres:reza.mosavi@localhost/BehshtiFoodData"

engine = create_engine(url)

session = sessionmaker(
    autocommit=False , autoflush=False ,bind=engine
)

def connectToDB():
    try:
        db = session()
        yield db
    finally:
        db.close()

Base = declarative_base()