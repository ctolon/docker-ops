#!/bin/bash

# This script extracts the GID of the docker group into .env to be used in the Jenkins container.

set -eo pipefail

docker_gid=$(getent group docker | cut -d: -f3)

echo $docker_gid

echo -e $"DOCKER_USER_GID=${docker_gid}" >> .env

echo "Docker GID extracted successfully."
