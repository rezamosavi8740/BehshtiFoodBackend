from fastapi import APIRouter ,Depends ,status
from database.database import connectToDB
from sqlalchemy.orm import Session
from Model import model
from Model import Values
import datetime

admin = APIRouter()

@admin.get("admin/food/{food-name}")
async def getFood(foodName:str ,
                  db:Session=Depends(connectToDB)):
    Model = db.query(model.Foods).\
        filter(foodName == model.Foods.name).first()
    if (Model is not None):
        return Model
    return status.HTTP_404_NOT_FOUND



@admin.get("admin/food/{price}")
async def getFood(price:int ,
                  db:Session=Depends(connectToDB)):
    Model = db.query(model.Foods).\
        filter(price == model.Foods.price).first()
    if (Model is not None):
        return Model
    return status.HTTP_404_NOT_FOUND


@admin.get("admin/food/{categories}")
async def getFood(categories:str ,
                  db:Session=Depends(connectToDB)):
    cat = db.query(model.Categories).\
        filter(categories == model.Categories.categories).first()

    # Model = db.query(model.Foods).\
    #     filter(cat == model.Foods.ca).first()
    if (cat is not None):
        return cat
    return status.HTTP_404_NOT_FOUND



@admin.get("admin/orders/{year}/{month}/{day}")
async def getOrders(year:str ,month:str ,day:str,
                  db:Session=Depends(connectToDB)):
    date = datetime.date.fromisoformat(year+"-"+month+"-"+day+"-")
    Model = db.query(model.Order).\
        filter(date == model.Order.date).first()
    if (Model is not None):
        return Model
    return status.HTTP_404_NOT_FOUND



@admin.get("admin/orders/{year}/{month}/{day}/{order-number}")
async def getOrders(year:str ,month:str ,day:str ,orderNumber:int ,
                  db:Session=Depends(connectToDB)):
    date = datetime.date.fromisoformat(year+"-"+month+"-"+day+"-")
    Model = db.query(model.Order).\
        filter(date == model.Order.date and orderNumber == model.Order.name).first()
    if (Model is not None):
        return Model
    return status.HTTP_404_NOT_FOUND


@admin.get("admin/orders/{delivered}")
async def getOrders(delivered:bool ,
                  db:Session=Depends(connectToDB)):
    Model = db.query(model.Order).\
        filter(delivered == model.Order.delivered).first()
    if (Model is not None):
        return Model
    return status.HTTP_404_NOT_FOUND


@admin.get("admin/orders/{order-number}")
async def getOrders(number:int ,
                  db:Session=Depends(connectToDB)):
    Model = db.query(model.Order).\
        filter(number == model.Order.name).first()
    if (Model is not None):
        return Model
    return status.HTTP_404_NOT_FOUND


@admin.get("admin/categories")
async def getOrders(db:Session=Depends(connectToDB)):
    Model = db.query(model.Order).all()
    if (Model is not None):
        return Model
    return status.HTTP_404_NOT_FOUND



@admin.post("admin/food")
async def addFood(food:Values.FoodValues,
                  db:Session=Depends(connectToDB)
                  ):
    Model = model.Foods()

    Model.name = food.name
    Model.price = food.price
    Model.number = food.number
    Model.categories = food.categories
    Model.imgURL = food.imgURL
    Model.description = food.description


    db.add(Model)
    db.commit()

    return status.HTTP_201_CREATED


@admin.post("admin/categories")
async def addCategories(categories: Values.CategoriesValues,
                  db: Session = Depends(connectToDB)
                  ):
    Model = model.Categories()

    Model.categories = categories.categories

    db.add(Model)
    db.commit()

    return status.HTTP_201_CREATED


@admin.post("admin/order")
async def addCategories(order: Values.OrderValues,
                  db: Session = Depends(connectToDB)
                  ):
    Model = model.Order()

    Model.name = order.name
    Model.price = order.price
    Model.date = order.date
    Model.delivered = order.delivered
    Model.foods = order.foods

    db.add(Model)
    db.commit()

    return status.HTTP_201_CREATED