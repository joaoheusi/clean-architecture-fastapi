import os
from typing import Any

from dotenv import load_dotenv

from src.modules.todos.implementations.beanie.document import TodoDocument
from src.modules.users.implementations.beanie.document import UserDocument

load_dotenv()

DOCUMENT_MODELS: list[Any] = [TodoDocument, UserDocument]
MONGODB_URL = os.getenv("MONGODB_URL")
