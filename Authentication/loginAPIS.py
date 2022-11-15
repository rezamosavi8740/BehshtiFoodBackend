from fastapi import APIRouter ,Depends
from database.database import connectToDB
from sqlalchemy.orm import Session
from Model import model

Login = APIRouter()

@Login.post("/Login")
def login(phoneNumber:str ,db:Session = Depends(connectToDB)):
    Model = db.query(model.users). \
        filter(model.users.phoneNumber == phoneNumber).first()

    if Model:
        return True

    return False
