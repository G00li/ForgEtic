run-docker: 
	docker compose up --build  

run-local:
	python3.12 manage.py runserver