import os
os.environ['kafkaHost'] = '40.114.93.145:9094'
os.environ['s3AccKey'] = 'public_key'
os.environ['s3SecretKey'] = 'public_secret'
os.environ['s3Host'] = 'http://bdservices-minio.idf-cts.com:9000'
os.environ['entities'] = '{"ora-gg-events": {"destBucket": "hila", "directoryInsideBucket": "or/events", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-reports": {"destBucket": "hila", "directoryInsideBucket": "or/reports", "isPartitionByYear": "True", "isPartitionByMonth": "True"},' \
           ' "ora-gg-eventsextra": {"destBucket": "hila", "directoryInsideBucket": "or/eventsextra", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-reportsextra": {"destBucket": "hila", "directoryInsideBucket": "or/reportsextra", "isPartitionByYear": "True", "isPartitionByMonth": "True"}, ' \
           ' "ora-gg-journals": {"destBucket": "hila", "directoryInsideBucket": "or/journals", "isPartitionByYear": "False", "isPartitionByMonth": "False"},' \
           ' "ora-gg-journalsextra": {"destBucket": "hila", "directoryInsideBucket": "or/journalsextra", "isPartitionByYear": "False", "isPartitionByMonth": "False"}, ' \
           ' "ora-gg-hila": {"destBucket": "hila", "directoryInsideBucket": "or/hila", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-shalisman": {"destBucket": "hila", "directoryInsideBucket": "or/shalisman", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-hilashalisman": {"destBucket": "hila", "directoryInsideBucket": "or/hilashalisman", "isPartitionByYear": "True", "isPartitionByMonth": "False"},' \
           ' "ora-gg-hilash": {"destBucket": "hila", "directoryInsideBucket": "or/hilash", "isPartitionByYear": "True", "isPartitionByMonth": "False"}}'
