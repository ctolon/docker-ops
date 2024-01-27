#!/bin/bash

# Bash script to delete a docker network for MLOps

set -e

docker network rm \
  mlops_network