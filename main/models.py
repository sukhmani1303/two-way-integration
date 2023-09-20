from main.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Customer Catalog Table (same as Stripe)
class customers(Base):
    __tablename__ = "customers"
    id = Column(String(60), primary_key = True, index = True) #uuid
    name = Column(String(50),  index = True)
    email = Column(String(50),  index = True)

# Table to store all Transaction Ids for reference
# class transactionId(Base):
#     __tablename__ = "transactionId"
#     tid = Column(String(60), primary_key = True, index = True)
#     type = Column(String(50),  index = True) # internal or external
#     id = Column(String(60), ForeignKey("customers.id"))
    