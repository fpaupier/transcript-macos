.PHONY: up pc install

install:
	uv sync
	uv run pre-commit install

up:
	uv run python -m src.cli

pc:
	uv run pre-commit run --all-files
