#!/bin/bash
# Bash Script to create a self-signed certificate for the docker registry

set -e

openssl req \
 -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key \
 -addext "subjectAltName = DNS:docker-registry-ml.com" \
 -x509 -days 365 -out certs/domain.crt

# openssl req -new -newkey rsa:2048 -nodes -keyout certs/registry.ctolon.ml.key -out certs/registry.ctolon.ml.csr
# openssl x509 -req -days 365 -in certs/registry.ctolon.ml.csr -signkey certs/registry.ctolon.ml.key -out certs/registry.ctolon.ml.crt
