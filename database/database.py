from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = "postgresql://postgres:reza.mosavi@localhost/BehshtiFoodData"
# url = "postgresql://postgres:reza.mosavi@localhost/data"

engine = create_engine(url)

session = sessionmaker(
    autocommit=False , autoflush=False ,bind=engine
)

# def connectToDB():
#     try:
#         db = session()
#         yield db
#     finally:
#         db.close()

Base = declarative_base()

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# url = "postgresql://postgres:reza.mosavi@localhost/data"
#
# engine = create_engine( url)
#
# session = sessionmaker(
#     autocommit=False , autoflush=False ,bind=engine
# )
#
# # def connectToDB():
# #     try:
# #         db = session()
# #         yield db
# #     finally:
# #         db.close()
#
# Base = declarative_base()


