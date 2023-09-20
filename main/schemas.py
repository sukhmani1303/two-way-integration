from pydantic import BaseModel

# General Schema for all 3 column data
class formData(BaseModel):
    id: str
    name: str
    email: str
    class Config():
        orm_mode = True

# Derived Schema to mark internal update
class fValidData(formData):
    internal_update : bool

# Simple schema for ID data
class lookup(BaseModel):
    id: str
    class Config():
        orm_mode = True