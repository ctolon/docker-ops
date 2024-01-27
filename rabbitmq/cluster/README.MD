# Rabbitmq Cluster

## How to run

```bash
bash set-permissions.sh # Only the first time for creating the folders and set permissions for the volumes
docker-compose up -d
```

you can access to the management console in http://<ip>:15672/ with the credentials.

HAProxy Provides a load balancer for the cluster.