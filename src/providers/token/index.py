from injector import Module, singleton, provider
from src.providers.token.contracts.interfaces.token import TokenProvider
from src.providers.token.implementations.fake.fake_token_provider import (
    FakeTokenProvider,
)


class FakeTokenProviderModule(Module):
    @singleton
    @provider
    def provide_fake_token_provider(self) -> TokenProvider:
        return FakeTokenProvider()
