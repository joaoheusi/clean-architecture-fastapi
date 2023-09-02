from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from src.configs.beanie_config import DOCUMENT_MODELS, MONGODB_URL
from src.providers.test_provider import config
from src.shared.server.routes import router

app = FastAPI()


@app.on_event("startup")
async def startup_event() -> None:
    await start_test()
    await start_beanie()


async def start_test() -> None:
    await config.set_variable(1)


async def start_beanie() -> None:
    database = AsyncIOMotorClient(MONGODB_URL).catodo
    await init_beanie(database=database, document_models=DOCUMENT_MODELS)


app.include_router(router)
