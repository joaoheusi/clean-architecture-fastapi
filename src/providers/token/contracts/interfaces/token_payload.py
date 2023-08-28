from typing import Any
from pydantic import BaseModel

from src.providers.token.contracts.enums.token_type import TokenType
from src.shared.contracts.enums.security_scope import SecurityScope


class TokenPayload(BaseModel):
    type: TokenType
    owner: str
    securityScope: SecurityScope
    extra: Any | None = None
