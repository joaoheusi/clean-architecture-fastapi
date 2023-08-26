import os

from dotenv import load_dotenv

from src.modules.todo.implementations.beanie.document import TodoDocument

load_dotenv()

DOCUMENT_MODELS = [TodoDocument]
MONGODB_URL = os.getenv("MONGODB_URL")
