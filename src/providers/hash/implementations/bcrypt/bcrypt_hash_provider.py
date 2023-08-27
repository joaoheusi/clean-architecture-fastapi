from bcrypt import gensalt, hashpw, checkpw
from src.providers.hash.contracts.interfaces.hash import HashProvider


class BcryptHashProvider(HashProvider):
    async def hash(self, payload: str) -> str:
        salt = gensalt()
        hashed = hashpw(payload.encode(), salt)

        return hashed.decode()

    async def compare(self, payload: str, hashed: str) -> bool:
        return checkpw(payload.encode(), hashed.encode())
