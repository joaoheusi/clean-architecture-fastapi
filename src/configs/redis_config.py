import os

from dotenv import load_dotenv

from pydantic import BaseModel

load_dotenv()


def cast_to_bool(value: str | bool) -> bool:
    if type(value) is bool:
        return value
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError("Value must be True or False")


REDIS_HOST = os.getenv("REDIS_HOST") or "localhost"
REDIS_PORT = int(os.getenv("REDIS_PORT") or 6379)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD") or None
REDIS_SSL = cast_to_bool(os.getenv("REDIS_SSL") or False)


class RedisConfig(BaseModel):
    host: str = "localhost"
    port: int = 6379
    password: str | None = None
    ssl: bool = False


loaded = {
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "password": REDIS_PASSWORD,
    "ssl": REDIS_SSL,
}

redis_config = RedisConfig(**loaded)
