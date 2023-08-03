from fastapi import FastAPI
from .api.chat.controller import router
from .api.chat.mydata import router as my_data_router

app = FastAPI(root_path="/")

app.include_router(router)
app.include_router(my_data_router)