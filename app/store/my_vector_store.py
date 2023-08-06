import os
import logging

from ..utils.singleton import Singleton
from ..config import config

from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma

logger = logging.getLogger(__name__)

def isEmpty(path):
    if os.path.exists(path) and not os.path.isfile(path):
  
        # Checking if the directory is empty or not
        if not os.listdir(path):
            logger.debug("Empty directory")
            result = True
        else:
            logger.debug("Not empty directory")
            result = False
    else:
        logger.debug("The path is either for a file or not valid")
        result = False
    return result

class MyVectorStoreIndex(metaclass=Singleton):

    def __init__(self):
        if isEmpty(config.VECTORSTORE_FOLDER):
            logger.debug("Persist folder is empty")
            #loader = TextLoader("/data/data.txt")  # Use this line if you only need data.txt
            loader = DirectoryLoader(config.DATA_FOLDER)

            if config.VECTORSTORE_PERSIST:
                self.__index = VectorstoreIndexCreator(
                    vectorstore_kwargs={"persist_directory": config.VECTORSTORE_FOLDER}
                ).from_loaders([loader])
            else:
                self.__index = VectorstoreIndexCreator().from_loaders([loader])

        else:
            logger.debug("Reusing existing index vector store")
            vectorstore = Chroma(
                persist_directory=config.VECTORSTORE_FOLDER,
                embedding_function=OpenAIEmbeddings(),
            )
            self.__index = VectorStoreIndexWrapper(vectorstore=vectorstore)

    @property
    def index(self):
        return self.__index
