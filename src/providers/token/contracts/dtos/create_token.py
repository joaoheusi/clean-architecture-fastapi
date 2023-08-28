from pydantic import BaseModel

from src.providers.token.contracts.interfaces.token_payload import TokenPayload


class CreateTokenDto(BaseModel):
    payload: TokenPayload
    ttl: int
