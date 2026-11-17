# Makefile for Timestamp Random Generator Library

.PHONY: help test clean install build check format license

help:
	@echo "Available commands:"
	@echo "  make install     - Install the package in editable mode"
	@echo "  make test        - Run unit tests"
	@echo "  make lint        - Run code linter (flake8)"
	@echo "  make format      - Format code with black"
	@echo "  make clean       - Remove generated files"
	@echo "  show-coverage    - Generate coverage report"

install:
	pip install -e .

test:
	cd tests && python test_random_gen.py

lint:
	flake8 randomgen/

format:
	black randomgen/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ .pytest_cache/ coverage.xml .coverage

show-coverage: install test
	pip install pytest-cov
	pytest --cov=randomgen --cov-report=html coverage_html_report