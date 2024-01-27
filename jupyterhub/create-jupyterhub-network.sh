#!/bin/bash
# Bash script to create a docker network for JupyterHub

set -e

docker network create \
  --driver=bridge \
  --subnet=172.13.0.0/16 \
  jupyterhub-net