from injector import Injector

from src.configs.container_config import FakeTodoRepositoryModule

container = Injector([FakeTodoRepositoryModule])
