# MLOps/DataOps/AIOps/DevOps Docker Servisleri

## Nginx ile Deploy

Eğer nginx ile Deploy edilmek isteniyorsa, Tüm MLOps Docker servislerini, `mlops_network` adlı ortak bir ağda çalıştırmak için: `create-mlops-network.sh` scriptini çalıştırarak bu ağı oluşturulur.

## Sadece I.P. ile Deploy

Eğer nginx olmadan deploy edilmek isteniyorsa, `docker-compose.yml` dosyalarında `ports` kısmı aktif edilerek port mapping sağlanır ve ardından `nginx` ile ilgili kısımlar silinir. Bu durumda, `mlops_network` adlı ortak bir ağ oluşturulmasına gerek yoktur.

```bash
bash create-mlops-network.sh
```