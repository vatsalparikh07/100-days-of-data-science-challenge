ifeq (,$(wildcard .env))
$(error .env file is missing. Please create one based on .env.example)
endif

include .env

export UV_PROJECT_ENVIRONMENT=.venv-rag
export PYTHONPATH = .

# --- Infrastructure --- 

local-infrastructure-up:
	docker compose -f docker-compose.yml up --build -d 

local-infrastructure-stop:
	docker compose -f docker-compose.yml stop

# --- Pipeline ---

run-ingestion-pipeline:
	uv run python -m tools.run_ingestion_pipeline

run-generation-pipeline:
	uv run python -m tools.run_generation_pipeline

run-agent-app:
	uv run python -m tools.agent_app
