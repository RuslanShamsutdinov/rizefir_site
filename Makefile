MANAGE := poetry run python manage.py

.PHONY: test
test:
	@poetry run pytest

.PHONY: setup
setup: db-clean install migrate


.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 python_django_orm_blog

dev:
	python manage.py runserver

install: .env
	@poetry install
make-migration:
	@$(MANAGE) makemigrations
migrate: make-migration
	@$(MANAGE) migrate

build: install migrate
