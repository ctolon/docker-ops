# Ön Adımlar

* Docker kurun. Sonrasında VM Max Count'ı arttırın ve swap alanını devre dışı bırakın:

```bash
$ sudo sysctl -w vm.max_map_count=262144
$ sudo swapoff -a
```

* Sonra Volumelerde izinleri bypass etmek için create-volume-dir.sh scriptini çalışıtırın:

```bash
$ bash create-volume.dir.sh
```

Bu script Dataların ve Sertifikaların compose dosyasında persistent volume tutmak için tanımlı olduğu yerde `/var/lib/ELK` altında gerekli klasörleri oluşturur var izinleri ayarlar. 

## ELK Aynı Makinede Environment Variables ile Kurmak

* `docker-compose.yml` isimli Docker Compose'u ayağı kaldırın:

```bash
docker-compose -f docker-compose.yml up -d
docker-compose -f docker-compose.yml logs -f setup
```

## Değiştirilebilecek Opsiyonlar Ve Dikkat edilmesi gereken noktalar

* Eğer yeni bir node eklenmek istenirse, `docker-compose.yml` dosyasında yer alan, aşağıdaki opsiyonlar:
  * `cluster.initial_master_nodes` güncellenebilir.
  * `discovery.seed_hosts` her bir node için güncellenmeli.
  * Kibana sectionunda `depends_on` bölümüne yeni node eklenmeli.
  * Yeni Node için `.env` dosyasında statik ip tanımlanmalı.
  * `create-volume-dir.sh` dosyasında `esdata<num>` şeklinde `chown` ve `mkdir` komutları için ekleme yapılmalı.

* Son olarak `setup` sectionunda yeni instance'ın da sertifikasının oluşması ve DNS için yeni node instance'ı bash scriptin ilgili yerine eklenmeli:

```bash
"  - name: esNUM\n"\
"    dns:\n"\
"      - esNUM\n"\
"      - localhost\n"\
"    ip:\n"\
"      - 127.0.0.1\n"\
```

## Ekstra Detaylar

* Bu konfigürasyonda Default olarak elasticsearch `172.76.0.0/24` subneti altında hizmet vermekte ve herbirine maintainable olması açısından bu subnette statik ip atanmıştır:

```bash
SETUP_IP=172.76.0.2
ES01_IP=172.76.0.3
ES02_IP=172.76.0.4
ES03_IP=172.76.0.5
KIBANA_IP=172.76.0.6
```

* Memlimit düşük tutulmuştur.
* Elastic ve Kibana için Default şifreler `test123` olarak belirlenmiştir.

## ELK Aynı Makinede .yml based kurmak

* `docker-compose.conf.yml` isimli Docker Compose'u ayağı kaldırın:

```bash
docker-compose -f docker-compose.yml up -d
docker-compose -f docker-compose.yml logs -f setup
```

## Değiştirilebilecek Opsiyonlar ve Dikkat Edilmesi gereken noktalar

* Her Bir Elasticsearch konfigürasyonu `conf` klasöründe tanımlanmıştır. `Shared` ile başlayan opsiyonlar her node için aynı olmalı, `Node` ile başlayanlar her Node için özeldir.
* Environment Variables'ta yapılması gereken değişiklikler, sadece aynı isimle `.yaml`'larda yer almakta. Eğer değişiklik yapılacaksa bu `.yaml` dosyalarını değiştirmek gerekir. Genel olarak tüm konfigler üst section ile aynıdır. 