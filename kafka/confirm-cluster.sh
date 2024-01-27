docker exec broker-1 \
    kafka-topics --bootstrap-server broker-1:9092 \
    --describe todos 