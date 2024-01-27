#!/bin/bash
# Basic bash script to generate certs (use in instead of built-in proxy certs)

set -e
openssl req -x509 -nodes -days 3650 -newkey rsa:1024 -keyout ./certs/key.pem -out ./certs/cert.pem