#!/bin/bash

# Author: Cevat Batuhan Tolon
# Script to create the volume directories for the ELK stack with permissions
# to allow the containers to write to them
# If you want add new nodes to the cluster, you need to add new directories here
# and then add them to the docker-compose.yml file

set -e 

TOP_LEVEL_DIR="/var/lib/ELK"

sudo mkdir -pv $TOP_LEVEL_DIR/esdata01 $TOP_LEVEL_DIR/esdata02 $TOP_LEVEL_DIR/esdata03 $TOP_LEVEL_DIR/kibanadata
sudo chmod -R 777 $TOP_LEVEL_DIR/esdata01 $TOP_LEVEL_DIR/esdata02 $TOP_LEVEL_DIR/esdata03 $TOP_LEVEL_DIR/kibanadata



