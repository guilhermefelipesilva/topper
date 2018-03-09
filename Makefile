install-development:
	pip install -r requirements/development.txt

install-staging:
	pip install -r requirements/staging.txt

install-production:
	pip install -r requirements/production.txt

run-dev:
	python manage.py runserver

# apply-patch:
# 	bumpversion patch