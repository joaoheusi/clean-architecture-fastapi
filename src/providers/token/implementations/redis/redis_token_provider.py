from secrets import token_hex
import redis
from src.providers.token.contracts.dtos.create_token import CreateTokenDto
import json
from src.providers.token.contracts.interfaces.token import TokenProvider
from src.providers.token.contracts.interfaces.token_payload import TokenPayload


class RedisTokenProvider(TokenProvider):
    def __init__(self) -> None:
        self.__redis = redis.Redis()

    async def create(self, data: CreateTokenDto) -> str:
        token = token_hex(64)
        self.__redis.set(
            name=token,
            value=data.payload.model_dump_json(by_alias=False),
            ex=data.ttl,
        )
        return token

    async def get(self, key: str) -> TokenPayload | None:
        payload = self.__redis.get(key)
        if type(payload) is not bytes:
            return None
        decoded = payload.decode("utf-8")
        dict_payload = json.loads(decoded)
        token_payload = TokenPayload(**dict_payload)
        try:
            return token_payload
        except Exception:
            return None

    async def expire(self, key: str) -> None:
        self.__redis.delete(key)
