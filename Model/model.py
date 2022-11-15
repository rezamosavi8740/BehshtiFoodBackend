from sqlalchemy import String ,Column ,Integer
from database.database import Base

class users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    phoneNumber = Column(String)
    password = Column(String)
    firstname  = Column(String)
    lastname = Column(String)
    token = Column(String)



