
deploy-migrate:
	python3.12 manage.py makemigrations
	python3.12 manage.py migrate

poetry-update: 
	poetry update


create-admin-automatico: 
	python3.12 manage.py createsuperuser --username admin --email admin@example.com 


create-admin-manual:
	python3.12 manage.py createsuperuser

run-docker: 
	docker compose up --build  

runserver:
	python3.12 manage.py runserver

Danger:
	python3.12 manage.py flush 

up:
	pip install poetry
	pip install django
	docker-compose up --build

init:
	make deploy-migrate
	make create-admin-automatico
	make up
