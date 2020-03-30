import boto3
from kafka import KafkaConsumer
import uuid
import json
from distutils.util import strtobool

def createS3Connection(s3AccKey, s3SecretKey, s3Host):
    s3 = boto3.resource('s3', aws_access_key_id=s3AccKey, aws_secret_access_key=s3SecretKey, endpoint_url=s3Host)
    return s3

def putMessageInS3(s3conn, destBucket, message, path):
    s3conn.Object(destBucket, path).put(Body=message)

def getDeltaFromKafka(kafkaHost):
    consumer = KafkaConsumer(group_id='my-group',
                             bootstrap_servers=[kafkaHost],
                             auto_offset_reset = 'earliest',
                             value_deserializer = lambda m: json.loads(m.decode('utf-8')))
    consumer.subscribe(pattern='^ora-gg.*')
    return consumer

def useConsumedData(kafkaConsumer, s3Conn, entities):
    for message in kafkaConsumer:
        directoryInsideBucket = entities[message.topic][1]
        destBucket = entities[message.topic][0]
        isPartitionByYear = entities[message.topic][2]
        isPartitionByMonth = entities[message.topic][3]
        preparedMessage = prepareDataRow(message.value)
        preparedMessageInJson = json.loads(preparedMessage)
        path = setPathToFile(directoryInsideBucket, preparedMessageInJson, strtobool(isPartitionByYear), strtobool(isPartitionByMonth))
        putMessageInS3(s3Conn, destBucket, preparedMessage, path)

def prepareDataRow(message):
    relevantMessage = message["payload"]
    if 'table' in relevantMessage:
        relevantMessage.pop('table')
    if 'current_ts' in relevantMessage:
        relevantMessage.pop('current_ts')
    if 'pos' in relevantMessage:
        relevantMessage.pop('pos')
    if 'op_type' in relevantMessage:
        if relevantMessage['op_type'] == 'U':
            relevantMessage['op_type'] == 'update'
        if relevantMessage['op_type'] == 'I':
            relevantMessage['op_type'] == 'insert'
        if relevantMessage['op_type'] == 'D':
            relevantMessage['op_type'] == 'delete'
    strRelevantMessage = json.dumps(relevantMessage)
    strRelevantMessage = strRelevantMessage.replace('op_type', 'je_operation')
    strRelevantMessage = strRelevantMessage.replace('op_ts', 'je_operation_date')
    return strRelevantMessage

def setPathToFile(directory, message, isYear, isMonth):
    path = directory + "/"
    if 'je_operation_date' in message:
        date = message['je_operation_date']
        if isYear:
            path += date[:4] + "/"
        if isMonth:
            path += date[5:7] + "/"
    path += str(uuid.uuid1())
    return path