i-development:
	pip install -r requirements/development.txt

i-staging:
	pip install -r requirements/staging.txt

i-production:
	pip install -r requirements/production.txt

i-test:
	pip install -r requirements/test.txt

run-dev:
	python manage.py runserver

run-worker:
	celery -A topper worker --loglevel=info

run-redis:
	docker start redis

apply-patch:
	bumpversion patch

apply-minor:
	bumpversion minor

apply-major:
	bumpversion major