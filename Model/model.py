from sqlalchemy import ForeignKey ,String ,Column ,Integer ,DATE ,Boolean
from database.database import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    phoneNumber = Column(String)
    password = Column(String)
    firstname  = Column(String)
    lastname = Column(String)
    token = Column(String)


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DATE)
    price = Column(Integer)
    name = Column(Integer)
    foods  = Column(Integer , ForeignKey("Foods.id"))
    delivered = Column(Boolean)
    foodOrders = relationship("Foods" ,back_populates = "orderFood")




class Foods(Base):
    __tablename__ = "Foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    imgURL  = Column(String)
    description = Column(String)
    categories = Column(Integer ,ForeignKey("Categories.id"))
    number = Column(Integer)
    orderFood = relationship("Foods" ,back_populates = "foodOrders")
    categoriesRel = relationship("Categories" ,back_populates = "foodRel")


class Categories(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True, index=True)
    categories = Column(String)
    foodRel = relationship("Foods" ,back_populates = "categoriesRel")
