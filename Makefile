.PHONY: build up down logs web tree clean-build

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

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help