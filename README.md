# TruthAI

Open-source AI assistant that prioritizes accuracy by combining LLMs with evidence retrieval.

This repository is a monorepo scaffold implementing Phase 1 initial auth + minimal frontend.

Quickstart (development):

1. Copy `.env.example` to `.env` and fill values.
2. Start DB and backend:
   docker compose -f docker-compose.dev.yml up --build -d
3. Run backend migrations and start app (inside backend):
   # if using poetry: poetry install && alembic upgrade head && uvicorn app.main:app --reload
4. Open API docs: http://localhost:8000/docs

What's included in this commit:
- backend: FastAPI app with JWT auth, SQLAlchemy models, basic tests, Dockerfile
- frontend: Next.js (TypeScript) app with login/register pages and AuthContext
- docker-compose.dev.yml for Postgres + Redis + backend
- .env.example listing required environment variables

I will continue by adding backend and frontend source files and explain each file as I create them.
