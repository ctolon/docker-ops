#!/bin/bash

set -e

# Create Users
# cbtolon
python3 create-user.py \
-f="Cevat Batuhan" \
-l="Tolon" \
-r="developer" \
-u="ctolon" \
-p="ctolon" \
-e="cbtolon@ctolon.ai";