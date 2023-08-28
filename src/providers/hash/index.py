from injector import Module, provider, singleton

from src.providers.hash.contracts.interfaces.hash import HashProvider
from src.providers.hash.implementations.bcrypt.bcrypt_hash_provider import (
    BcryptHashProvider,
)


class BcryptHashProviderModule(Module):
    @singleton
    @provider
    def provide_bcrypt_hash_provider(self) -> HashProvider:
        return BcryptHashProvider()
