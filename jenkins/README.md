# Kurulum Aşamaları

1- Öncelikle `create-jenkins.dir.sh` scripti çalıştırılarak klasörler oluşturulur.
2- `extract-docker-gid.sh` ile hostun docker idsi .env ye eklenerek docker build edilirken host ile maplenir.
3- `create-ssh-key.sh` scripti ile sertifikalar oluşturulur. pubkey compose'da agent için ayarlanır.
4- `docker compose build` ile build yapılır.
5- `docker compose up -d` ile servisler başlatılır.
6- Jenkins ayağı kaldırıldıktan sonra node eklenir. Eklenirken  Host Key Verification Strategy Non seçilir. Remote root directory /home/jenkins/agent olarak seçilir. Ayrıca java path kesinlikle doğru ayarlanmalı (compose'da var, slave'ın java pathi) Port vs. ayarlanır external ise. ssh private key eklenir.


Launch method: SSH
Host: Slave IP

bash create-jenkins-dir.sh && bash extract-docker-gid.sh && docker compose build && docker compose up -d