from fastapi import FastAPI

from src.providers.test_provider import config

app = FastAPI()


@app.on_event("startup")
async def startup_event() -> None:
    await start_test()


async def start_test():
    await config.set_variable(1)
