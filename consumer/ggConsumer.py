from kafka import KafkaConsumer
import json
from distutils.util import strtobool
import s3Utils

def getDeltaFromKafka(kafkaHost):
    consumer = KafkaConsumer(group_id='my-group',
                             bootstrap_servers=[kafkaHost],
                             auto_offset_reset = 'earliest',
                             value_deserializer = lambda m: json.loads(m.decode('utf-8')))
    consumer.subscribe(pattern='^ora-gg.*')
    return consumer

def useConsumedData(kafkaConsumer, s3Conn, entities):
    for message in kafkaConsumer:
        directoryInsideBucket = entities[message.topic]['directoryInsideBucket']
        destBucket = entities[message.topic]['destBucket']
        isPartitionByYear = strtobool(entities[message.topic]['isPartitionByYear'])
        isPartitionByMonth = strtobool(entities[message.topic]['isPartitionByMonth'])
        preparedMessage = prepareDataRow(message.value)
        path = s3Utils.setPathToFile(directoryInsideBucket, preparedMessage, isPartitionByYear, isPartitionByMonth)
        s3Utils.putMessageInS3(s3Conn, destBucket, preparedMessage, path)

def prepareDataRow(message):
    operations = {"U": "update", "I": "insert", "D": "delete"}
    relevantMessage = message["payload"]
    relevantMessage.pop('table') if 'table' in relevantMessage else None
    relevantMessage.pop('current_ts') if 'current_ts' in relevantMessage else None
    relevantMessage.pop('pos') if 'pos' in relevantMessage else None
    if 'op_type' in relevantMessage:
        relevantMessage['op_type'] = operations[relevantMessage['op_type']]
        relevantMessage['je_operation'] = relevantMessage['op_type']
        relevantMessage.pop('op_type')
    if('op_ts') in relevantMessage:
        relevantMessage['je_operation_date'] = relevantMessage['op_ts']
        relevantMessage.pop('op_ts')
    return relevantMessage
