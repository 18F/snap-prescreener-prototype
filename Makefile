install: install-dev

install-dev:
	pip install pipenv
	pipenv install --dev

install-prod:
	pip install pipenv
	pipenv install

style-check:
	pipenv run flake8 --max-line-length=160

security-check:
	pipenv run bandit -r snap_financial_factors

check-all: style-check security-check

serve: serve-local

serve-local:
	pipenv run gunicorn "app:create_app()" --reload

serve-prod: install-prod
	pipenv run gunicorn "app:create_app()"

deploy: deploy-cf

deploy-cf:
	cf push

logs: logs-cf

logs-cf:
	./set_app_name.sh
	cf logs ${APP_NAME}
