from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

allowed_origins = [
    origin.strip() for origin in settings.allowed_origins.split(",") if origin.strip()
]

app = FastAPI(
    title="Document Copilot API",
    version="0.1.0",
    description="Backend API for document ingestion, retrieval, and chat workflows.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "app": settings.app_name}


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Document Copilot backend is running."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
