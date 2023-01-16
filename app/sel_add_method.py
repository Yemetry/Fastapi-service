from sqlalchemy.orm import sessionmaker

from setting_db import engine
import models, valid

models.Base.metadata.create_all(bind=engine)


# This method opens a connection with the database then there is a search by user id then it returns the full user
# data namely phone email and login
def get_id(id: int):
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = db()
    user = session.query(models.User).filter(models.User.id == id).first()
    return user


# adding a new user after receiving data recording and saving to the database
def add_user(user: valid.User):
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = db()
    db_user = models.User(login=user.login, email=user.email, phone=user.phone)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
