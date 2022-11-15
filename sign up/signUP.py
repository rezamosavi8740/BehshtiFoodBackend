from fastapi import APIRouter ,Depends
from database.database import connectToDB
from sqlalchemy.orm import Session
from Model import model

signup = APIRouter()

@signup.post("/signup")
async def addUser(db:Session=Depends(connectToDB)):
