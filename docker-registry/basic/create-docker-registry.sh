#!/bin/bash

docker run -d \
  -e REGISTRY_HTTP_ADDR=0.0.0.0:5005 \
  -p 5005:5005 \
  --name docker-registry-test \
  --restart=always \
  registry:2