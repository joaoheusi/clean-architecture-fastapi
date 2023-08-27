from abc import ABC, abstractmethod


class HashProvider(ABC):
    @abstractmethod
    async def hash(self, payload: str) -> str:
        raise Exception("Not implemented")

    @abstractmethod
    async def compare(self, payload: str, hashed: str) -> bool:
        raise Exception("Not implemented")
