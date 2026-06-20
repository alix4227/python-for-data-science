docker run -d \
  --name formationdjango \
  -e POSTGRES_PASSWORD=secret \
  -p 5433:5432 \
  postgres:17-alpine
docker exec -it formationdjango psql -U postgres -c "CREATE USER djangouser WITH PASSWORD 'secret';"
docker exec -it formationdjango psql -U postgres -c "CREATE DATABASE formationdjango OWNER djangouser;"