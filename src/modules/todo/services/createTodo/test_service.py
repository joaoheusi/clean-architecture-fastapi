import asyncio
import unittest

from src.modules.todo.contracts.dtos.createTodo_dto import CreateTodoDto
from src.modules.todo.implementations.fake.fake_todo_repository import (
    FakeTodoRepository,
)
from src.modules.todo.services.createTodo.service import CreateTodoService


class TestCreateTodoService(unittest.TestCase):
    fake_todo_repository = FakeTodoRepository()
    create_todo_service = CreateTodoService(fake_todo_repository)
    event_loop = asyncio.get_event_loop()

    def test_correct(self):
        data = CreateTodoDto(
            **{
                "title": "title",
                "description": "description",
                "is_done": False,
            }
        )
        response = self.event_loop.run_until_complete(
            self.create_todo_service.handle(data)
        )
        assert response.title == data.title
        assert response.description == data.description
        assert response.is_done == data.is_done
