from pydantic import BaseModel
from typing import List
import datetime

class UserValues(BaseModel):

    phoneNumber:str
    password:str
    firstname:str
    lastname:str
    token:str


class OrderValues(BaseModel):

    date:datetime
    price:int
    name:int
    foods:List[int]
    delivered:bool


class FoodValues(BaseModel):

    name:str
    price:int
    imgURL:str
    description:str
    categories:List[int]
    number:int


class CategoriesValues(BaseModel):

    categories:str
