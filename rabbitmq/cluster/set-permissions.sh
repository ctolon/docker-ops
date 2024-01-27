#!/bin/bash
# Author: Cevat Batuhan Tolon
# Create datadir and set permissions for keep datas
# You can run this script before the docker-compose up -d command as one time.

set -e

# Create datadir for keep datas
sudo mkdir -pv data/rabbitmq-01/logs
sudo mkdir -pv data/rabbitmq-02/logs
sudo mkdir -pv data/rabbitmq-03/logs

sudo chown root:root data
sudo chmod 777 data/rabbitmq-01/logs
sudo chmod 777 data/rabbitmq-02/logs
sudo chmod 777 data/rabbitmq-03/logs


