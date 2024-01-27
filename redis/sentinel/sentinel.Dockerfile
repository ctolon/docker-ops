ARG REDIS_TAG
FROM redis:${REDIS_TAG}

ADD ./conf/sentinel/sentinel.conf /etc/redis-config/

# Set Permissions to sentinel.conf
RUN chmod -R 0777 /etc/redis-config
RUN chown redis:redis /etc/redis-config/sentinel.conf