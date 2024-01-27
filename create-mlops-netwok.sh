#!/bin/bash

# Bash script to create a docker network for MLOps w/ nginx-proxy

set -e

docker network create \
  --driver=bridge \
  --subnet=172.48.0.0/16 \
  mlops_network