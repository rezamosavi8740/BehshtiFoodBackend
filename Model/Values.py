from pydantic import BaseModel
import datetime

# class UserValues(BaseModel):
#
#     phoneNumber:str
#     password:str
#     firstname:str
#     lastname:str
#     token:str
#
#     class Config:
#         orm_mode = True
#

class Values(BaseModel):
    phoneNumber:str
    # password:str
    # lastname:str
    # firstname:str
    # token:str
    class Config:
        orm_mode = True



class OrderValues(BaseModel):

    date:datetime.date
    price:int
    name:int
    foods:int
    delivered:bool

    class Config:
        orm_mode = True



class FoodValues(BaseModel):

    name:str
    price:int
    imgURL:str
    description:str
    categories:int
    number:int
    orderFood :list[OrderValues] = []
    class Config:
        orm_mode = True

class CategoriesValues(BaseModel):

    categories:str
    foodRel : list[FoodValues] = []

    class Config:
        orm_mode = True


# from pydantic import BaseModel
#
# from typing import Optional, List
#
#
# class Requests(BaseModel):
#
#     timeRequests:str
    # foodNameRequests:str
    # priceRequests:int



# class Food(BaseModel):
#     mainCategory: str
#     secondeCategory: str
#     foodName: str
#     price: int
#     imgName: str
#     imgID: int



# class Users(BaseModel):
#
#     username:str
#     password:str
#     email:str
#     age:int
#     sex:bool

# class UsersValues(BaseModel):
#
#     username: str
#     password: str
#     email: str
#     age: int
#     sex: bool
#
#     class Config:
#         orm_mode = True


    # RequestsID: List[Requests]
    # User = Requests

# class RequestsValues(BaseModel):
#
#     timeRequests:str
#     # foodNameRequests:List[Food]
#     # priceRequests:List[Users]
#     # userRequests = Users
#     # foodR = Food
#     # class config:
#     #     orm_mode = True
#     # owner = Users
#
# # class FoodValues(BaseModel):
# #     mainCategory:str
# #     secondeCategory:str
# #     foodName:str
# #     price:int
# #     imgName:str
# #     imgID:int
# #     requests = Requests
#
# from pydantic import BaseModel
#
#
# class ItemBase(BaseModel):
#     title: str
#     description: str
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(BaseModel):
#     id: int
#     owner_id: int
#     title: str
#     description: str
#     class Config:
#         orm_mode = True
#
#
