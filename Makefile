.PHONY: docs

install: 
	python -m pip install uv
	uv venv
	uv pip install -e . marimo pandas polars pytest mktestdocs

pypi:
	uv build
	uv publish

check:
	uv run pytest

docs:
	uv run marimo export html-wasm demo.py --output docs --mode edit