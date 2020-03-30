from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='40.114.93.145:9094',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
while True:
    producer.send('ora-gg-events', {"schema": "field", "payload": {"table": "emet.events", "op_type": "U", "op_ts": "2020-03-29 16:59:28.00000", "current_ts": "2020-03-29 17:59:28.00000", "pos": "555", "relevant_field": "hello"}})
    producer.send('ora-gg-reports', {"schema": "field", "payload": {"table": "emet.events", "op_type": "U", "op_ts": "2020-03-29 16:59:28.00000", "current_ts": "2020-03-29 17:59:28.00000", "pos": "555", "relevant_field": "hello"}})
    print("sent")
    time.sleep(1)