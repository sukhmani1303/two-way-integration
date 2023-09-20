import uvicorn
from main import models
from routes import routes
from fastapi import FastAPI
from main.database import engine

app = FastAPI() # creating FastAPI object

models.Base.metadata.create_all(engine) # creating/ loading all models (tables)

app.include_router(routes.router) # attaching routes

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = 8080) # running server
