import openai
from ...config import config
import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)


router = APIRouter(tags=["Chat OpenAI"])
openai.api_key = config.OPENAI_API_KEY

# Assistant context
assistant_context = ""

messages = [{
    "role" : "system",
    "content" : assistant_context
  }]


@router.post("/call")
def call(content: str) -> str:
    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response_content = response.choices[0].message.content

    messages.append({"role": "assistant", "content": response_content})

    return response_content
