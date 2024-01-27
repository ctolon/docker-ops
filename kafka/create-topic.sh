docker exec broker-1 \
    kafka-topics --bootstrap-server broker-1:9092 \
             --create \
             --topic todos --partitions 6 --replication-factor 3