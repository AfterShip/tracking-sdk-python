.PHONY: build

install:
	poetry install

test:
	poetry run pytest tests/ -v

record:
	poetry run pytest tests/ --vcr-record=new_episodes

format:
	poetry run ruff check --fix
	poetry run ruff format

build:
	poetry build
