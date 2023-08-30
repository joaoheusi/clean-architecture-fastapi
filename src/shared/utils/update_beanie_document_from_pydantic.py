from typing import TypeVar

from beanie import Document
from pydantic import BaseModel

T = TypeVar("T", bound=Document)
U = TypeVar("U", bound=BaseModel)


async def update_beanie_document_from_pydantic(document: T, pydantic_model: U) -> None:
    for key, value in pydantic_model.model_dump().items():
        setattr(document, key, value)
