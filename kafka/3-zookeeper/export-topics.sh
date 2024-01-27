#!/bin/bash

docker cp ./create-topics.sh kafka_1:/tmp/kafka/create-topics.sh
docker cp ./tla-topics.txt kafka_1:/tmp/kafka/tla-topics.txt

docker exec kafka_1 bash /tmp/kafka/create-topics.sh