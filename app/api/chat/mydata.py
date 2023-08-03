import os
import logging
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

from ...config import config
from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Chat LangChain"])

os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY
# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False


chat_history = []


@router.post("/question")
def question(query: str) -> str:
    return question_about_my_data(query)


def question_about_my_data(query):
    if PERSIST and os.path.exists("persist"):
        print("Reusing index...\n")
        vectorstore = Chroma(
            persist_directory="persist", embedding_function=OpenAIEmbeddings()
        )
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        loader = TextLoader("/data/data.txt")  # Use this line if you only need data.txt
        # loader = DirectoryLoader("/data/")

    if PERSIST:
        index = VectorstoreIndexCreator(
            vectorstore_kwargs={"persist_directory": "persist"}
        ).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    result = chain({"question": query, "chat_history": chat_history})

    chat_history.append((query, result["answer"]))

    return result["answer"]
