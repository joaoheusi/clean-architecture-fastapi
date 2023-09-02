from typing import Any

from fastapi.routing import APIRouter

from src.modules.todos.routers.todos_router import todos_router
from src.modules.users.routers.users_router import users_router
from src.providers.test_provider import config

router = APIRouter()


@router.get("/ping")
async def ping() -> dict[str, Any]:
    variable = await config.get_variable()
    return {"message": "pong", "variable": variable}


router.include_router(todos_router)
router.include_router(users_router)
