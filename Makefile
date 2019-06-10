#!/bin/bash

start:
	pipenv run python manage.py runserver

migrate:
	pipenv run python manage.py migrate

createsuperuser:
	pipenv run python manage.py createsuperuser

rm-db:
	rm db.sqlite3
