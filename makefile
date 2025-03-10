include .env
export $(shell sed -E '/^\s*#/d;/^\s*$$/d;s/=.*//' .env)

# standart commands for docker-compose managment
start:
	docker-compose up --remove-orphans
upd:
	docker-compose up --remove-orphans -d
upb:
	docker-compose up --remove-orphans --build
upbd:
	docker-compose up --remove-orphans --build -d
stop:
	docker-compose stop
clear:
	docker-compose down --remove-orphans -v
logs:
	docker-compose logs -f


# comands for migration-container
msg?=
mgr:
	docker-compose run migration sh -c "alembic revision --autogenerate -m '$(msg)'"
	docker-compose run migration sh -c "alembic upgrade head"
	docker-compose stop migration
