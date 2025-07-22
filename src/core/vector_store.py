import os, faiss, pickle, threading
from src.core.config import settings
from langchain_community.embeddings import OpenAIEmbeddings

_INDEX_PATH = os.path.join("data", "faiss.index")
_LOCK = threading.Lock()


def _load() -> tuple[faiss.IndexFlatL2, list[str]]:
    if os.path.exists(_INDEX_PATH):
        index, meta = pickle.load(open(_INDEX_PATH, "rb"))
    else:
        index, meta = faiss.IndexFlatL2(1536), []
    return index, meta


def add_texts(texts: list[str]) -> None:
    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    vecs = embeddings.embed_documents(texts)
    with _LOCK:
        index, meta = _load()
        index.add(vecs)
        meta.extend(texts)
        pickle.dump((index, meta), open(_INDEX_PATH, "wb"))
