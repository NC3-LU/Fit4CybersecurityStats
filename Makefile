SHELL := /bin/bash

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default."
	@echo "Try 'make help'"

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	poetry install

activate:
	poetry shell

html:
	poetry run python generate_html.py

markdown:
	poetry run python generate_markdown.py

runserver:
	poetry run python runserver.py

update:
	poetry install --no-dev

heroku:
	git push heroku master

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
