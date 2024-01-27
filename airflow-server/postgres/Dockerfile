
ARG POSTGRESQL_VERSION
ARG POSTGRES_PASSWORD
ARG POSTGRES_HOST_AUTH_METHOD
FROM postgres:${POSTGRESQL_VERSION}

RUN echo "=================================================" \
    && echo "PASSWORD=$POSTGRES_PASSWORD" \
    && echo "=============================================="
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}