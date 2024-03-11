FROM postgres:latest
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=luxonis_db
COPY create_table.sql /docker-entrypoint-initdb.d/create_table.sql