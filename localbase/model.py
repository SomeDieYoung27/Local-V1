from langchain_community.chat_models import ChatOllama
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_core.language_models import BaseLanguageModel
from langchain_groq import ChatGroq

from localbase.config import Config

def create_llm() -> BaseLanguageModel:
    if Config.Model_USE_LOCAL:
        return ChatOllama(
            model = Config.MODEL.LOCAL_LLM,
            temperature=Config.Model.TEMPERATURE,
            keep_alive="1h",
            max_tokens=Config.Model.MAX_TOKENS,
            
        )
    else:
        return ChatGroq(
            temperature=Config.Model.TEMPERATURE,
            model_name = Config.MODEL.REMOTE_LLM,
            max_tokens = Config.Model.MAX_TOKENS,
            
        )
    

def create_embeddings() -> FastEmbedEmbeddings:
    return FastEmbedEmbeddings(model_name = Config.MODELS.EMBEDDINGS)


def create_reranker() -> FlashrankRerank:
    return FlashrankRerank(
        model = Config.Model.RERANKER,
    )

