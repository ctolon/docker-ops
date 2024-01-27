# MinIO S3 Cluster Setup

[minio setup](https://min.io/docs/minio/linux/operations/installation.html)

- Add nginx static ip to hosts as:

```shell
172.48.0.10    minio
```

- for another host, add directly host ip:
- 
```shell
<Host Machine IP>    minio
```

- Access On UI with default nginx.conf:

```shell
http://minio:9001
```

- Access on UI nginx-80.conf (also you must define port mapping on nginx docker service as `"80:80"`):

```shell
http://minio
```