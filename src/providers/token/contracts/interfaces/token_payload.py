from typing import Any
from pydantic import BaseModel

from src.providers.token.contracts.enums.token_type import TokenType


class TokenPayload(BaseModel):
    type: TokenType
    owner: str
    securityScope: str
    extra: Any | None = None
