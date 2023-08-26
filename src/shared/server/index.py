from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from src.configs.beanie_config import DOCUMENT_MODELS, MONGODB_URL
from src.providers.test_provider import config

app = FastAPI()


@app.on_event("startup")
async def startup_event() -> None:
    await start_test()
    await start_beanie()


async def start_test():
    await config.set_variable(1)


async def start_beanie():
    database = AsyncIOMotorClient(MONGODB_URL).catodo
    await init_beanie(database=database, document_models=DOCUMENT_MODELS)
