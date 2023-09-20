from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# db url <username>:<password>@localhost:<port>/<database>
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:01uvsingh@localhost:5433/zenskardb' 

engine = create_engine(SQLALCHEMY_DATABASE_URL) # creating an engine to communicate with DB

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit = False, autoflush = False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
