.PHONY: install test lint
install:
	pip install -r requirements.txt
test:
	pytest -q
lint:
	ruff check .
