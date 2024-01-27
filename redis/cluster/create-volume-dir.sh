#!/bin/bash

# Author: Cevat Batuhan Tolon
# Script to create the volume directories for the Redis Cluster stack with permissions
# to allow the containers to write to them
# If you want add new nodes to the cluster, you need to add new directories here
# and then add them to the docker-compose.yml file

set -e 

TOP_LEVEL_DIR="/var/lib/RedisCluster"

sudo mkdir -pv \
    $TOP_LEVEL_DIR/redis_1 \
    $TOP_LEVEL_DIR/redis_2 \
    $TOP_LEVEL_DIR/redis_3 \
    $TOP_LEVEL_DIR/redis_4 \
    $TOP_LEVEL_DIR/redis_5 \
    $TOP_LEVEL_DIR/redis_6


sudo chmod -R 777 \
    $TOP_LEVEL_DIR/redis_1 \
    $TOP_LEVEL_DIR/redis_2 \
    $TOP_LEVEL_DIR/redis_3 \
    $TOP_LEVEL_DIR/redis_4 \
    $TOP_LEVEL_DIR/redis_5 \
    $TOP_LEVEL_DIR/redis_6



