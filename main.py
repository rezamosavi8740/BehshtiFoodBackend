from fastapi import FastAPI ,Depends
from sqlalchemy.orm import Session
# from Authentication.loginAPIS import Login
from admin import admin
from Model import Values ,model

# from database.database import connectToDB



app = FastAPI()

# app.include_router(admin.admin)
#
# @app.post("/")
# async def addFood(food:Values.FoodValues,
#                   db:Session=Depends(connectToDB)
#                   ):
#     Model = model.Foods()
#
#     Model.name = food.name
#     Model.price = food.price
#     Model.number = food.number
#     Model.categories = food.categories
#     Model.imgURL = food.imgURL
#     Model.description = food.description
#
#
#     db.add(Model)
#     db.commit()
#
#     # return status.HTTP_201_CREATED
#
#     return {
#         "status":"YES"
#     }
#
# @app.post("admin/categories")
# async def addCategories(categories: Values.CategoriesValues,
#                   db: Session = Depends(connectToDB)
#                   ):
#     Model = model.Categories()
#
#     Model.categories = categories.categories
#
#     db.add(Model)
#     db.commit()
#
#     return "status.HTTP_201_CREATED"
from database.database import session
def connectToDB():
    try:
        db = session()
        yield db
    finally:
        db.close()
#
@app.post("/user")
async def adduser(user:Values.Values,
                  db: Session = Depends(connectToDB)
                  ):

    Model = model.Users()
    Model.phoneNumber = user.phoneNumber
    # # Model.firstname = user.firstname
    # # Model.lastname = user.lastname
    # # Model.password = user.password
    # # Model.token = user.token
    #
    db.add(Model)
    db.commit()
    return "YES"

# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session
#
# from Model import code, model, Values
# from database.database import session, engine
#
# model.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
#
# # Dependency
# from database.database import session
# def get_db():
#     db = session()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/users/", response_model=Values.User)
# def create_user(user: Values.UserCreate, db: Session = Depends(get_db)):
#     db_user = code.get_user_by_email(db, phoneNumber=user.phoneNumber)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return code.create_user(db=db, user=user)

#
# @app.get("/users/", response_model=list[Values.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = code.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=Values.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = code.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/")
# def create_item_for_user(
#     user_id: int, item: Values.Item, db: Session = Depends(get_db)
# ):
#
#     Model = model.Item()
#
#     Model.title = item.title
#     Model.description = item.description
#     Model.owner_id = user_id
#
#     db.add(Model)
#     db.commit()
#
#     return "code.create_user_item(db=db, item=item, user_id=user_id)"
#
#
# @app.get("/items/", response_model=list[Values.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = code.get_items(db, skip=skip, limit=limit)
#     return items

# @app.post("admin/order")
# async def addCategories(order: Values.OrderValues,
#                   db: Session = Depends(connectToDB)
#                   ):
#     Model = model.Order()
#
#     Model.name = order.name
#     Model.price = order.price
#     Model.date = order.date
#     Model.delivered = order.delivered
#     Model.foods = order.foods
#
#     db.add(Model)
#     db.commit()
#
#     return "status.HTTP_201_CREATED"


# @app.get('/')
# async def first_api():
#     return 'firstapi'