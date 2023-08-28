from injector import Module, singleton, provider
from src.providers.token.contracts.interfaces.token import TokenProvider
from src.providers.token.implementations.fake.fake_token_provider import (
    FakeTokenProvider,
)
from src.providers.token.implementations.redis.redis_token_provider import (
    RedisTokenProvider,
)


class FakeTokenProviderModule(Module):
    @singleton
    @provider
    def provide_fake_token_provider(self) -> TokenProvider:
        return FakeTokenProvider()


class RedisTokenProviderModule(Module):
    @singleton
    @provider
    def provide_redis_token_provider(self) -> TokenProvider:
        return RedisTokenProvider()
