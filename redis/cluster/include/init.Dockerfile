ARG REDIS_TAG
FROM redis:${REDIS_TAG}

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]