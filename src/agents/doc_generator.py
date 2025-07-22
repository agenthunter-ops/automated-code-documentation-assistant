from pathlib import Path
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from src.core.config import settings

_llm = ChatOpenAI(model_name=settings.OPENAI_MODEL, temperature=0.1, openai_api_key=settings.OPENAI_API_KEY)

_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert software engineer who writes crystal-clear docstrings "
            "(Google style). Place the docstring inside triple double-quotes.",
        ),
        ("human", "{code}"),
    ]
)


async def generate_docstring(code: str) -> str:
    msg = _PROMPT.format_prompt(code=code)
    resp = await _llm.achat([msg])
    return resp.content.strip().strip('"').strip()
