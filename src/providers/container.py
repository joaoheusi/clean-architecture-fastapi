from injector import Injector

from src.configs.container_config import (
    BeanieTodoRepositoryModule,
)

container = Injector([BeanieTodoRepositoryModule])
