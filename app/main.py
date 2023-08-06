import logging
import yaml

from fastapi import FastAPI
from .api.chat.controller import router
from .api.chat.mydata import router as my_data_router
from .store.my_vector_store import MyVectorStoreIndex
from .config import config

app = FastAPI(root_path="/")

app.include_router(router)
app.include_router(my_data_router)


@app.on_event("startup")
async def startup():
    setup_yaml()
    logger = logging.getLogger(__name__)
    try:
        MyVectorStoreIndex()
        logger.info("MyVectorStoreIndex initialized")
    except Exception as ex:
        logger.exception("Error initializating VectorStore: %s", str(ex))


def setup_yaml():
    with open(config.LOGGING_CONFIG_FILE,  "r") as f:
        yaml_config = yaml.safe_load(f.read())
        logging.config.dictConfig(yaml_config)
