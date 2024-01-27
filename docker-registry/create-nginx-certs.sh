#!/bin/bash
# Bash script to create nginx certs

set -e

openssl req -newkey rsa:2048 -nodes -keyout nginx/privkey.pem -x509 -days 3650 -out nginx/fullchain.pem