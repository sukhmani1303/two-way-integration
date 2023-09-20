from sqlalchemy.orm import Session
from main import models, schemas

def update(db:Session, fdata:schemas.formData):
    
    id_1 = db.query(models.customers).filter(models.customers.id ==fdata.id).one_or_none()

    if id_1 is None:
        return None
    
    id_1.name = fdata.name
    id_1.email = fdata.email
    db.commit()

    return id_1

