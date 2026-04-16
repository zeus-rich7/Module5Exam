run:
	docker compose up --build -d
	docker compose exec -T postgres psql -U postgres -d recipie_bot < pre-setup.sql
