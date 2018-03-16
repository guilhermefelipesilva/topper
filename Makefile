install-development:
	pip install -r requirements/development.txt

install-staging:
	pip install -r requirements/staging.txt

install-production:
	pip install -r requirements/production.txt

install-test:
	pip install -r requirements/test.txt

run-dev:
	python manage.py runserver

run-staging:
	export ENVIROMENT=staging && python manage.py runserver

run-production:
	export ENVIROMENT=production && python manage.py runserver

run-worker-dev:
	export BROKER_URL="redis://localhost:6379/0" && celery -A topper worker --loglevel=info

run-redis:
	docker start redis

apply-patch:
	bumpversion patch

apply-minor:
	bumpversion minor

apply-major:
	bumpversion major