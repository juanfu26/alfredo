from fastapi import FastAPI
from .api.chat.controller import router

app = FastAPI(root_path="/")

app.include_router(router)