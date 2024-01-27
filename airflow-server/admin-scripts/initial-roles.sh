#!/bin/bash

set -e

# Create roles
python3 create-role.py -r user
python3 create-role.py -r developer
python3 create-role.py -r senior_developer