#!/bin/bash
# Bash script to create admin user for docker registry

set -e

docker run \
  --entrypoint htpasswd \
  httpd:2 -Bbn admin ctolonml > auth/htpasswd


#htpasswd -Bc htpasswd admin