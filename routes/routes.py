import json
import stripe
from sqlalchemy.orm import Session
from main import database,schemas, models
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repository import outward, k_producer, inward
from fastapi import APIRouter, Depends, HTTPException,status

keys = json.load(open('keys.json'))

stripe.api_key = keys['STRIPE_SECRET_KEY']
stripe_webhook_secret = keys['WEBHOOK_SECRET']

get_db = database.get_db

router = APIRouter()

@router.post('/outward_sync/update', status_code = status.HTTP_200_OK, tags = ['outward_sync'])
async def all(fdata : schemas.formData, db : Session = Depends(get_db)):
    q1 = outward.update(db, fdata)

    if q1 is not None:
        item_data = dict(fdata)
        k_producer.add_item_to_queue(item_data)
        return JSONResponse(content={"message": "Customer Catalog Updated Successfully!"}, status_code=200)

    return HTTPException(status_code=404, detail= f"Customer with id : {fdata.id} not found!")

@router.post("/inward_sync/update",status_code = status.HTTP_200_OK ,tags = ['inward_sync'])
async def stripe_webhook(event: dict, db : Session = Depends(get_db)):
        try:
            if event['type'] == 'customer.updated':

                customer = event['data']['object']
              
                resp = inward.sync_customer_to_local_catalog(customer, db)

                if resp:
                    return JSONResponse(content={"message": "Event received and processed!"}, status_code=200)
                
                else:
                    return JSONResponse(content={"message": "Cannot find Customer with submitted id!"}, status_code=404)
            
            else:
                return JSONResponse(content={"message": "Invalid Event!"}, status_code=404)

        except Exception as e:
            return HTTPException(status_code=500, detail=str(e))

  
@router.post('/update_data', status_code = status.HTTP_200_OK ,tags = ['other'])
def all_data(id: schemas.lookup, db : Session = Depends(get_db)):
    data_1 = db.query(models.customers).filter(models.customers.id ==id.id).first()

    if data_1 is None:
        return JSONResponse(content = {"message" : "Customer with ID not found!"}, status_code=404 )
    
    return JSONResponse(content = {"id": data_1.id, "name" : data_1.name, "email" : data_1.email}, status_code=200 )

@router.post('/get_all', status_code = status.HTTP_200_OK ,tags = ['other'])
def all_data(db : Session = Depends(get_db)):
    data_1 = db.query(models.customers).all()

    if data_1 is None:
        return None

    data_main = jsonable_encoder(data_1)

    return JSONResponse(content = data_main, status_code=200)


    
    


