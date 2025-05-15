import re
from operator import itemgetter
from typing import List

from langchain.schema.runnable import RunnablePassthrough
from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.tracers.stdout import ConsoleCallbackHandler
from langchain_core.vectorstores import VectorStoreRetriever

from localbase.config import Config
from localbase.session_history import SessionHistory

SYSTEM_PROMPT = """
Utilize the provided contextual information to respond to the user question.
If the answer is not found within the context, state that the answer cannot be found.
Prioritize concise responses (maximum of 3 sentences) and use a list where applicable.
The contextual information is organized with the most relevant source appearing first.
Each source is separated by a horizontal rule (---).

Context:
{context}

Use markdown formatting where appropriate.
"""

