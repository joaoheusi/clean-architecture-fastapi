from fastapi.routing import APIRouter

from src.modules.todos.routers.todos_router import todos_router
from src.providers.test_provider import config
from src.shared.server.index import app

router = APIRouter()


@router.get("/ping")
async def ping():
    variable = await config.get_variable()
    return {"message": "pong", "variable": variable}


app.include_router(router)
app.include_router(todos_router)
