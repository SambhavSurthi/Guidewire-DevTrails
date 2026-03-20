# GigGuard X — Makefile
# =======================
# Usage: make <command>
# Requires: Docker, Docker Compose, Python 3.11+, Node.js 18+

.PHONY: help dev dev-stop build test migrate seed lint clean logs

BACKEND_DIR := backend
FRONTEND_DIR := frontend

# ── HELP ──────────────────────────────────────────────────────────
help:
	@echo ""
	@echo "  GigGuard X — Available Commands"
	@echo "  ================================"
	@echo "  make dev          Start full dev environment (Docker)"
	@echo "  make dev-stop     Stop all containers"
	@echo "  make build        Build production Docker images"
	@echo "  make migrate      Run Alembic database migrations"
	@echo "  make seed         Seed database with demo data"
	@echo "  make train        Train all ML models"
	@echo "  make rag-build    Build RAG FAISS index"
	@echo "  make test         Run all tests (backend + frontend)"
	@echo "  make test-back    Run backend tests only"
	@echo "  make test-front   Run frontend tests only"
	@echo "  make lint         Run linters (ruff + eslint)"
	@echo "  make logs         Tail all container logs"
	@echo "  make clean        Remove containers, volumes, build artifacts"
	@echo "  make shell-back   Open shell in backend container"
	@echo "  make shell-db     Open psql shell"
	@echo ""

# ── DEVELOPMENT ───────────────────────────────────────────────────
dev:
	@echo "Starting GigGuard X development environment..."
	@cp -n .env.example .env 2>/dev/null || true
	docker compose -f docker-compose.dev.yml up -d postgres redis
	@echo "Waiting for database..."
	@sleep 3
	$(MAKE) migrate
	$(MAKE) seed
	$(MAKE) train
	$(MAKE) rag-build
	docker compose -f docker-compose.dev.yml up -d
	@echo ""
	@echo "  GigGuard X is running!"
	@echo "  Frontend:  http://localhost:5173"
	@echo "  Backend:   http://localhost:8000"
	@echo "  API Docs:  http://localhost:8000/docs"
	@echo "  Admin:     admin@gigguard.in / admin123"
	@echo "  Worker:    ravi@gigguard.in / worker123"
	@echo ""

dev-stop:
	docker compose -f docker-compose.dev.yml down

logs:
	docker compose -f docker-compose.dev.yml logs -f

# ── DATABASE ──────────────────────────────────────────────────────
migrate:
	@echo "Running database migrations..."
	cd $(BACKEND_DIR) && \
		docker compose -f ../docker-compose.dev.yml exec backend \
		alembic upgrade head || \
		(pip install -r requirements.txt -q && alembic upgrade head)

migrate-create:
	cd $(BACKEND_DIR) && alembic revision --autogenerate -m "$(MSG)"

migrate-down:
	cd $(BACKEND_DIR) && alembic downgrade -1

seed:
	@echo "Seeding demo data..."
	cd $(BACKEND_DIR) && python scripts/seed_demo_data.py

shell-db:
	docker compose -f docker-compose.dev.yml exec postgres \
		psql -U gigguard -d gigguard_db

# ── ML & RAG ──────────────────────────────────────────────────────
train:
	@echo "Training ML models..."
	cd $(BACKEND_DIR) && python -m app.ml.train_risk
	cd $(BACKEND_DIR) && python -m app.ml.train_income
	cd $(BACKEND_DIR) && python -m app.ml.train_fraud
	@echo "ML models trained and saved."

rag-build:
	@echo "Building RAG FAISS index..."
	cd $(BACKEND_DIR) && python -m app.rag.embeddings build
	@echo "RAG index built."

# ── TESTING ───────────────────────────────────────────────────────
test: test-back test-front
	@echo "All tests passed!"

test-back:
	@echo "Running backend tests..."
	cd $(BACKEND_DIR) && \
		pytest tests/ -v --cov=app --cov-report=term-missing --cov-fail-under=70

test-front:
	@echo "Running frontend tests..."
	cd $(FRONTEND_DIR) && npm run test -- --watchAll=false

# ── LINTING ───────────────────────────────────────────────────────
lint: lint-back lint-front

lint-back:
	cd $(BACKEND_DIR) && ruff check app/ && ruff format --check app/

lint-front:
	cd $(FRONTEND_DIR) && npm run lint

format:
	cd $(BACKEND_DIR) && ruff format app/
	cd $(FRONTEND_DIR) && npm run format

# ── BUILD (PRODUCTION) ────────────────────────────────────────────
build:
	@echo "Building production images..."
	docker compose build
	@echo "Build complete."

# ── SHELL ACCESS ──────────────────────────────────────────────────
shell-back:
	docker compose -f docker-compose.dev.yml exec backend bash

shell-front:
	docker compose -f docker-compose.dev.yml exec frontend sh

# ── CLEANUP ───────────────────────────────────────────────────────
clean:
	@echo "Cleaning up..."
	docker compose -f docker-compose.dev.yml down -v
	docker compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name node_modules -exec rm -rf {} + 2>/dev/null || true
	rm -f $(BACKEND_DIR)/app/rag/rag_index.faiss
	rm -f $(BACKEND_DIR)/app/rag/rag_chunks.pkl
	rm -f $(BACKEND_DIR)/app/ml/models/*.pkl
	@echo "Clean complete."

clean-db:
	docker compose -f docker-compose.dev.yml down -v postgres
	docker volume rm gigguard_postgres_data 2>/dev/null || true
	@echo "Database volume removed."

# ── QUICK DEMO ────────────────────────────────────────────────────
demo-trigger:
	@echo "Simulating heavy rain in Hyderabad..."
	curl -s -X POST http://localhost:8000/api/v1/admin/trigger-disruption \
		-H "Content-Type: application/json" \
		-H "Authorization: Bearer $$(curl -s -X POST http://localhost:8000/api/v1/auth/login \
			-H 'Content-Type: application/json' \
			-d '{"email":"admin@gigguard.in","password":"admin123"}' | python3 -c 'import sys,json;print(json.load(sys.stdin)["access_token"])')" \
		-d '{"event_type":"heavy_rain","city":"Hyderabad","zone":"Central","value":38.0,"duration_hours":3.5}' \
		| python3 -m json.tool
	@echo "Check http://localhost:5173/claims to see auto-triggered claims!"
