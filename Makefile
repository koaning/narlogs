install: 
	python -m pip install uv
	uv venv
	uv pip install -e . marimo pandas polars pytest mktestdocs

pypi:
	uv build
	uv publish