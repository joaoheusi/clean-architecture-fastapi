from injector import Injector

from src.configs.container_config import (
    BeanieTodoRepositoryModule,
    BeanieUsersRepositoryModule,
)

container = Injector([BeanieTodoRepositoryModule, BeanieUsersRepositoryModule])
