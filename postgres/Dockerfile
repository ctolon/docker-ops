ARG POSTGRESQL_VERSION
ARG POSTGRES_PASSWORD
ARG POSTGRES_HOST_AUTH_METHOD

FROM postgres:14.6

RUN echo "=================================================" \
    && echo "PASSWORD=$POSTGRES_PASSWORD" \
    && echo "=============================================="
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}