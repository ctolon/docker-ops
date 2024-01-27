# Monitoring

Ref: https://github.com/Einsteinish/Docker-Compose-Prometheus-and-Grafana/tree/master

- Prometheus (metrics database) http://<host-ip>:9090
- Prometheus-Pushgateway (push acceptor for ephemeral and batch jobs) http://<host-ip>:9091
- AlertManager (alerts management) http://<host-ip>:9093
- Grafana (visualize metrics) http://<host-ip>:3000
- NodeExporter (host metrics collector)
- cAdvisor (containers metrics collector)
- Caddy (reverse proxy and basic auth provider for prometheus and alertmanager)

https://engineering.teknasyon.com/cadvisor-ile-docker-konteyner-metrik-takibi-600a62705769