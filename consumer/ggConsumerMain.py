import ggConsumer
import json

# something in my computer doesn't allow me to set environment variables so here i use regular variables instead
kafkaHost = '40.114.93.145:9094'
s3AccKey = 'public_key'
s3SecretKey = 'public_secret'
s3Host = 'http://bdservices-minio.idf-cts.com:9000'
entities = '{"ora-gg-events": ["hila", "or/events", "True", "False"], "ora-gg-reports": ["hila", "or/reports", "True", "True"]}'

# kafkaHost = os.environ.get('kafkaHost')
# s3AccKey = os.environ.get('s3AccKey')
# s3SecretKey = os.environ.get('s3SecretKey')
# s3Host = os.environ.get('s3Host')
# entities = os.environ.get('entities')

dictEntities = json.loads(entities)

rawData = ggConsumer.getDeltaFromKafka(kafkaHost)
s3Conn = ggConsumer.createS3Connection(s3AccKey, s3SecretKey, s3Host)
ggConsumer.useConsumedData(rawData, s3Conn, dictEntities)