import logging

from fastapi import APIRouter
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from ...store.my_vector_store import MyVectorStoreIndex


logger = logging.getLogger(__name__)

router = APIRouter(tags=["Chat LangChain"])

chat_history = []


@router.post("/question")
def question(query: str) -> str:
    return question_about_my_data(query)


def question_about_my_data(query):
    index = MyVectorStoreIndex().index
    print(index)
    logger.warn(index)

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    result = chain({"question": query, "chat_history": chat_history})

    chat_history.append((query, result["answer"]))

    return result["answer"]
