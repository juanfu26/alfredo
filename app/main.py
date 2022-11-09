from fastapi import FastAPI
from api import whController

app = FastAPI(root_path="/alfredo")

app.include_router(whController.router)

@app.get("/")
def root():
    return {"message": "Hello world"}

