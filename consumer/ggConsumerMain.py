import ggConsumer
import s3Utils
import json

# something in my computer doesn't allow me to set environment variables so here i use regular variables instead
kafkaHost = '40.114.93.145:9094'
s3AccKey = 'public_key'
s3SecretKey = 'public_secret'
s3Host = 'http://bdservices-minio.idf-cts.com:9000'
entities = '{"ora-gg-events": {"destBucket": "hila", "directoryInsideBucket": "or/events", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-reports": {"destBucket": "hila", "directoryInsideBucket": "or/reports", "isPartitionByYear": "True", "isPartitionByMonth": "True"},' \
           ' "ora-gg-eventsextra": {"destBucket": "hila", "directoryInsideBucket": "or/eventsextra", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-reportsextra": {"destBucket": "hila", "directoryInsideBucket": "or/reportsextra", "isPartitionByYear": "True", "isPartitionByMonth": "True"}, ' \
           ' "ora-gg-journals": {"destBucket": "hila", "directoryInsideBucket": "or/journals", "isPartitionByYear": "False", "isPartitionByMonth": "False"},' \
           ' "ora-gg-journalsextra": {"destBucket": "hila", "directoryInsideBucket": "or/journalsextra", "isPartitionByYear": "False", "isPartitionByMonth": "False"}, ' \
           ' "ora-gg-hila": {"destBucket": "hila", "directoryInsideBucket": "or/hila", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-shalisman": {"destBucket": "hila", "directoryInsideBucket": "or/shalisman", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-hilashalisman": {"destBucket": "hila", "directoryInsideBucket": "or/hilashalisman", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-hilash": {"destBucket": "hila", "directoryInsideBucket": "or/hilash", "isPartitionByYear": "True", "isPartitionByMonth": "False"}}'

linkTopicToS3Location = json.loads(entities)

kafkaConsumer = ggConsumer.getDeltaFromKafka(kafkaHost)
s3Conn = s3Utils.createS3Connection(s3AccKey, s3SecretKey, s3Host)
ggConsumer.useConsumedData(kafkaConsumer, s3Conn, linkTopicToS3Location)
