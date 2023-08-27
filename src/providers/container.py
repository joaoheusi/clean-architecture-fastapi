from injector import Injector

from src.configs.container_config import (
    BeanieTodoRepositoryModule,
    BeanieUsersRepositoryModule,
)
from src.providers.hash.index import BcryptHashProviderModule

container = Injector(
    [BeanieTodoRepositoryModule, BeanieUsersRepositoryModule, BcryptHashProviderModule]
)
