from main import models
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

def sync_customer_to_local_catalog(customer, db : Session): 
    id_1 = db.query(models.customers).filter(models.customers.id ==customer['id']).one_or_none()

    if id_1 is None:
        return None
    
    id_1.name = customer['name']
    id_1.email = customer['email']
    db.commit()

    return {"message" : "Synced With Stripe's Customer Catalog!"}