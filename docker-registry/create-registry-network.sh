#!/bin/bash
# Bash script to create a docker network for MLOps

set -e

docker network create \
  --driver=bridge \
  --subnet=172.79.0.0/16 \
  ml_registry_network