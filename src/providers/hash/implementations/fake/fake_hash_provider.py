from src.providers.hash.contracts.interfaces.hash import HashProvider


class FakeHashProvider(HashProvider):
    async def hash(self, payload: str) -> str:
        return f"{payload}+{payload}"

    async def compare(self, payload: str, hashed: str) -> bool:
        return hashed.split("+")[0] == payload
