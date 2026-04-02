.PHONY: install-dev lint test run

install-dev:
	pip install -e .[dev]

lint:
	ruff check src tests

test:
	pytest

run:
	python main.py
