run:
	docker compose up --build -d
	docker compose run --rm bot alembic stamp head
	docker compose run --rm bot alembic revision --autogenerate -m "migration check"
	docker compose run --rm bot alembic upgrade head
