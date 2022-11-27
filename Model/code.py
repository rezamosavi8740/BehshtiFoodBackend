from sqlalchemy.orm import Session

from . import model, Values


def get_user(db: Session, user_id: int):
    return db.query(model.Users).filter(model.Users.id == user_id).first()


def get_user_by_email(db: Session, phoneNumber: str):
    return db.query(model.Users).filter(model.Users.phoneNumber == phoneNumber).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: Values.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = model.Users(phoneNumber=user.phoneNumber, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Values.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: Values.ItemBase, user_id: int):
#     db_item = Values.Item(**item.dict() ,owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item