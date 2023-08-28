from injector import Injector

from src.configs.container_config import (
    BeanieTodoRepositoryModule,
    BeanieUsersRepositoryModule,
)
from src.providers.hash.index import BcryptHashProviderModule
from src.providers.token.index import FakeTokenProviderModule

container = Injector(
    [
        BeanieTodoRepositoryModule,
        BeanieUsersRepositoryModule,
        BcryptHashProviderModule,
        FakeTokenProviderModule,
    ]
)
