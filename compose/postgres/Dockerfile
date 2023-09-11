FROM postgres:14.8-bullseye

# Environment variables
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV DB_NAME=${DB_NAME}

# Create the database and user
RUN mkdir -p /docker-entrypoint-initdb
RUN echo "CREATE DATABASE ${DB_NAME} WITH ENCODING 'UTF8';" >> /docker-entrypoint-initdb/init.sql
RUN echo "CREATE USER ${POSTGRES_USER} WITH ENCRYPTED PASSWORD '${POSTGRES_PASSWORD}';" >> /docker-entrypoint-initdb/init.sql
RUN echo "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${POSTGRES_USER};" >> /docker-entrypoint-initdb/init.sql

