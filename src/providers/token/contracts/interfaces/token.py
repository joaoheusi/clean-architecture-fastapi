from abc import ABC, abstractmethod

from src.providers.token.contracts.dtos.create_token import CreateTokenDto
from src.providers.token.contracts.interfaces.token_payload import TokenPayload


class TokenProvider(ABC):
    @abstractmethod
    async def create(self, data: CreateTokenDto) -> str:
        raise Exception("Not implemented")

    @abstractmethod
    async def get(self, key: str) -> TokenPayload | None:
        raise Exception("Not implemented")

    @abstractmethod
    async def expire(self, key: str) -> None:
        raise Exception("Not implemented")
