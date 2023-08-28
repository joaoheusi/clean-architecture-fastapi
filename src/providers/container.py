from injector import Injector

from src.configs.container_config import (
    BeanieTodoRepositoryModule,
    BeanieUsersRepositoryModule,
)
from src.providers.hash.index import BcryptHashProviderModule
from src.providers.token.index import RedisTokenProviderModule

container = Injector(
    [
        BeanieTodoRepositoryModule,
        BeanieUsersRepositoryModule,
        BcryptHashProviderModule,
        RedisTokenProviderModule,
    ]
)
