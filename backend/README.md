# Backend FastAPI Service

## Quick start

1. Open a terminal in `backend/`.
2. Install dependencies and sync the package: `uv sync`
3. Create or update `.env` from `.env.example`.
4. Run the app locally: `uv run uvicorn app.main:app --reload`

## Database migrations

- Create a new migration: `uv run alembic revision --autogenerate -m "<message>"`
- Apply migrations: `uv run alembic upgrade head`

## Notes

- `backend/app/config.py` is the single source of runtime settings.
- `backend/app/main.py` is the FastAPI entrypoint.
- Use `.env` and `pydantic-settings` rather than `os.getenv`.
