# Airflow Worker Node Compose

Prod. Airflow için Celery Executor ile çalışmak için makineler arası bütünleşik olacak şekilde docker compose konfigürasyonları.

`192.168.1.132` makinesi master node ayarlanmıştır.

`192.168.0.24` ve `192.168.1.131` makineleri worker node olarak ayarlanmıştır.

ekstra eklenecek worker nodeların docker compose dosyası aynı şekilde oluşturulabilir.

Yeni bir worker node oluşturulduktan sonra ana `docker-compose.yml` dosyasının extra hosts kısmına eklenmelidir.

```yaml

  extra_hosts:
    - "worker-1.131:192.168.1.131" 
    - "worker-0.24:192.168.0.24"
    # Buraya eklenir.
```