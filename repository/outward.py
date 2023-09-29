from sqlalchemy.orm import Session
from main import models, schemas
import string 
import random
from main.database import *

# def custid(db : Session):
#     symb = """~!@#$%^&*()_-+={[}}|\:;<,>.?/"""
#     characters = string.ascii_letters + string.digits + symb
#     token = ''.join(random.choice(characters) for _ in range(8))
#     rec = db.query(models.customers).filter(models.customers.id == token).first()
#     while(rec!=None):
#         token = ''.join(random.choice(characters) for _ in range(8))
#         rec = db.query(models.customers).filter(models.customers.id == token).first()
#     return token


def update(db:Session, fdata:schemas.formData):
    
    id_1 = db.query(models.customers).filter(models.customers.id ==fdata.id).one_or_none()

    if id_1 is None:
        return None
    
    id_1.name = fdata.name
    id_1.email = fdata.email
    db.commit()

    return id_1

def add(fdata:schemas.addFormData):

    print("in function !!")

    # db : Session = Depends(get_db)
    with SessionLocal() as db:
    
        id_1 = db.query(models.customers).filter(models.customers.email == fdata.email).one_or_none()

        if id_1 is None:
            q_add = models.customers(id = fdata.id, name = fdata.name, email = fdata.email)
            db.add(q_add)
            db.commit()
            db.refresh(q_add) 

            return q_add
        
        return None


def delete(db:Session,fdata:schemas.lookup):

    print("in function !!")

    id_1 = db.query(models.customers).filter(models.customers.id == fdata.id).one_or_none()

    if id_1 is not None:
        q3 = db.query(models.customers).filter(models.customers.id == fdata.id).delete()
        db.commit()
        return q3
    
    return None


def check_user(db : Session, email : str):
    user = db.query(models.customers).filter(models.customers.email == email).one_or_none()
    return user


def search_stripe(email : str, cust_list : list ):
    for cust in cust_list:
        if email == cust['email']:
            return cust
    return None

def search_stripe_id(id : str, cust_list : list ):
    for cust in cust_list:
        if id == cust['id']:
            return cust
    return None