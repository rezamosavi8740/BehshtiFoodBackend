from sqlalchemy import ForeignKey ,String ,Column ,Integer ,DATE ,Boolean
from database.database import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    phoneNumber = Column(String)
    # password = Column(String)
    # firstname  = Column(String)
    # lastname = Column(String)
    # token = Column(String)


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
    orderFood = relationship("Order" ,back_populates = "foodOrders")
    categoriesRel = relationship("Categories" ,back_populates = "foodRel")


class Categories(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True, index=True)
    categories = Column(String)
    foodRel = relationship("Foods" ,back_populates = "categoriesRel")


# from sqlalchemy import ForeignKey ,Boolean ,Column ,Integer ,String ,Float
# from database.database import Base
# from sqlalchemy.orm import relationship
#
# class Users(Base):
#     __tablename__ = "Users"
#
#     id = Column(Integer ,primary_key =True ,index = True)
#     username = Column(String)
#     password = Column(String)
#     email = Column(String)
#     age = Column(Integer)
#     sex = Column(Boolean)
    # RequestsID  = Column(Integer ,ForeignKey("Requests.id"))
    # User = relationship("Requests" ,back_populates = "userRequests")
#
# # class Foods(Base):
# #     __tablename__ = "Foods"
# #
# #     id = Column(Integer, primary_key=True, index=True)
# #     mainCategory = Column(String)
# #     secondeCategory = Column(String)
# #     foodName = Column(String)
# #     price = Column(Integer)
# #     imgName = Column(String)
# #     imgID = Column(Integer)
# #     request = relationship("Requests" ,back_populates = "foodR")
#
#
#
# class Requests(Base):
#     __tablename__ = "Requests"
#
#     id = Column(Integer ,primary_key =True ,index = True)
#     timeRequests = Column(String)
#     # foodNameRequests  = Column(String ,ForeignKey("Foods.foodName"))
#     # priceRequests  = Column(Integer ,ForeignKey("Foods.price"))
#     userRequests = relationship("Users" ,back_populates = "User")
#     # foodR =   ("Foods" ,back_populates = "userRequests")
#     owner  = Column(Integer ,ForeignKey("Users.id"))


#
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
#
# from database.database import Base
#

# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")
#
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="items")