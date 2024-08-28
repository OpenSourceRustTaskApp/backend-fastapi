.PHONY: build up down logs web db config tree clean-build migrate-revision migrate-upgrade help

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

web:
	docker-compose exec web bash

db:
	docker-compose exec db bash

config:
	docker-compose config

tree:
	tree -I 'venv|__pycache__|mysql-data' .

clean-build:
	docker-compose down -v
	docker system prune -af
	docker volume prune -f
	docker-compose build --no-cache
	docker-compose up -d

migrate-revision: ## Generate a new migration revision
	docker-compose run --rm web alembic revision --autogenerate -m "$(message)"

migrate-upgrade: ## Apply all pending migrations
	docker-compose run --rm web alembic upgrade head

migrate-downgrade: ## Downgrade database to the previous revision
	docker-compose run --rm web alembic downgrade -1

migrate-history: ## Show migration history
	docker-compose run --rm web alembic history

migrate-current: ## Show current revision
	docker-compose run --rm web alembic current

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help