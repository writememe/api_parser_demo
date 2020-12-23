
.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | \
	sort | \
	awk -F ':.*?## ' 'NF==2 {printf "\033[35m  %-25s\033[0m %s\n", $$1, $$2}'

all: lint-all ## Perform all linting checks, security checks and tests
lint-all:	black pylama bandit ## Perform all linting and security checks (black, pylama and bandit).

black: ## Format code using black
	@echo "--- Performing black reformatting ---"
	black . --check

pylama:	## Perform python linting using pylama
	@echo "--- Performing pylama linting ---"
	pylama .

bandit:	## Perform python code security checks using bandit
	@echo "--- Performing bandit code security scanning ---"
	bandit 00*/ -v --exclude ./venv --recursive --format json --verbose -s B101

.PHONY: venv
venv: ## Install virtualenv, create virtualenv, install requirements for Python 3
	@echo "--- Creating virtual environment and installing requirements (Python3.x) ---"
	virtualenv --python=`which python3` venv
	. venv/bin/activate
	pip install -r requirements.txt


