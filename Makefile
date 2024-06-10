run-docker : 
	docker compose up --build  

run-local :
	python manage.py runserver