from datetime import datetime

from app.dto.example import ExampleCreateDTO, ExampleDTO


class ExampleService:
    """
    Сервисный слой для работы с примерами.
    Использует хранилище в памяти для демонстрации.
    """

    _examples: dict[int, dict] = {}
    _next_id: int = 1

    @classmethod
    async def create(cls, data: ExampleCreateDTO) -> ExampleDTO:
        """Создает новую запись в хранилище в памяти."""
        new_id = cls._next_id
        new_example_data = {
            "id": new_id,
            "name": data.name,
            "created_at": datetime.utcnow(),
        }
        cls._examples[new_id] = new_example_data
        cls._next_id += 1
        return ExampleDTO(**new_example_data)

    @classmethod
    async def get_all(cls) -> list[ExampleDTO]:
        """Возвращает все записи из хранилища в памяти."""
        return [ExampleDTO(**e) for e in cls._examples.values()]
