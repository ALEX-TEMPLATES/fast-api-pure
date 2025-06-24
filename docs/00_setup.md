# Настройка Проекта

## Environment Setup

1.  **Создайте виртуальное окружение**:
    ```bash
    python -m venv .venv
    ```
2.  **Активируйте виртуальное окружение**:
    -   Windows (Git Bash/PowerShell):
        ```bash
        source .venv/Scripts/activate
        ```
    -   Linux/macOS:
        ```bash
        source .venv/bin/activate
        ```
3.  **Установите зависимости** (если используете `uv`):
    ```bash
    uv sync
    ```
    (Примечание: `uv sync` работает с `pyproject.toml` напрямую).

4.  **Запустите приложение**:
    ```bash
    uvicorn src.main:app --reload
