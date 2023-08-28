from src.providers.token.contracts.dtos.create_token import CreateTokenDto
from src.providers.token.contracts.interfaces.token import TokenProvider
from src.providers.token.contracts.interfaces.token_payload import TokenPayload
from secrets import token_hex


class FakeTokenProvider(TokenProvider):
    __tokens: dict[str, TokenPayload] = {}

    async def create(self, data: CreateTokenDto) -> str:
        token = token_hex(64)
        self.__tokens[token] = data.payload
        return token

    async def get(self, key: str) -> TokenPayload | None:
        return self.__tokens.get(key, None)

    async def expire(self, key: str) -> None:
        del self.__tokens[key]
