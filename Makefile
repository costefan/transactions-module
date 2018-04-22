build: requirements.txt
		docker-compose build

.PHONY: run
run:
		docker-compose up

down:
		docker-compose down

stop:
		docker-compose stop