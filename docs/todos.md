# Project Todo List

## Phase 1: Backend foundation

- [ ] Set up the FastAPI application structure under `backend/app/` with `main.py`, `config.py`, and initial router layout.
- [ ] Implement environment configuration using the single source of truth in `backend/app/config.py` and fail fast on missing required values.
- [ ] Add Supabase auth integration and current-user dependency for protected endpoints.
- [ ] Define the core database models for users, chats, source documents, chunks, and retrieval metadata.
- [ ] Create Alembic migrations for the schema and review them before applying.
- [ ] Add database session management and typed repository/query helpers for backend services.

## Phase 2: Document ingestion and processing

- [ ] Build the ingestion pipeline for SEC/financial document intake and parsing.
- [ ] Extract text from downloaded filings and normalize content before chunking.
- [ ] Chunk source documents into manageable passages suitable for embeddings and semantic search.
- [ ] Generate embeddings for chunks using the OpenAI embedding model.
- [ ] Store document metadata and chunk records in Supabase/Postgres with pgvector support.
- [ ] Add ingestion validation to ensure references, chunk counts, and document metadata are consistent.

## Phase 3: Retrieval and hybrid search

- [ ] Implement semantic retrieval using Supabase `pgvector` for embedding similarity search.
- [ ] Implement keyword retrieval using Postgres full-text search.
- [ ] Combine vector and full-text results with Reciprocal Rank Fusion (RRF) in Python.
- [ ] Fetch source passages and document metadata needed to ground answers in retrieved content.
- [ ] Add citation-aware retrieval so the answer can reference exact source passages.

## Phase 4: Chat and assistant logic

- [ ] Build the chat API endpoints for creating conversations, sending messages, and returning answers.
- [ ] Orchestrate the retrieval + LLM answer flow for each user request.
- [ ] Implement grounding checks to ensure responses are tied to retrieved content and cite sources.
- [ ] Add prompt/instruction templates for the assistant behavior and answer format.
- [ ] Handle streaming or async response patterns consistent with FastAPI / API contract requirements.
- [ ] Validate the output structure and citation extraction before returning to the client.

## Phase 5: Backend quality and testing

- [ ] Add unit tests for ingestion logic, retrieval behavior, citation extraction, and grounding enforcement.
- [ ] Keep fast tests isolated from network and external DB dependencies.
- [ ] Add integration tests only for live Supabase/OpenAI flows behind explicit markers.
- [ ] Run backend linting and test checks to keep the service stable.
- [ ] Review code against repo rules: small functions, no unnecessary abstractions, no silent config fallbacks.

## Phase 6: Frontend implementation

- [ ] Set up the Vite + React + TypeScript frontend app and project config.
- [ ] Add environment handling through `frontend/lib/env.ts` and validate required variables at startup.
- [ ] Implement auth flow with Supabase email sign-in and bearer token handling via the API client.
- [ ] Build the chat interface for conversation history, input, and answer display.
- [ ] Create document upload and source document listing screens if required by the product flow.
- [ ] Use the shared API client for requests and keep HTTP handling consistent with the company standards.
- [ ] Verify the frontend with TypeScript checks and manual browser validation.

## Phase 7: Deployment and operations

- [ ] Configure Railway backend and frontend deployment settings.
- [ ] Set up environment variables and secrets for Supabase, OpenAI, and app config.
- [ ] Run database migrations in the proper backend environment before production release.
- [ ] Confirm CORS, auth, and API connectivity between frontend and backend.
- [ ] Add operational monitoring and basic logging to support debug and incident response.

## Phase 8: Final validation

- [ ] End-to-end test the document ingestion flow from upload to retrieval to answer generation.
- [ ] Verify that all answers include grounded citations and relevant retrieval context.
- [ ] Confirm the app works for the expected user flows in the browser.
- [ ] Review the final implementation against the repo-wide AGENTS instructions and clean up any policy violations.

## Recommended execution order

1. Backend foundation and database schema
2. Ingestion pipeline and chunk storage
3. Retrieval and citation logic
4. Assistant chat orchestration and grounding
5. Frontend UI and auth
6. Deployment setup and end-to-end validation
