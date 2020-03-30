import os
os.environ['kafkaHost'] = '40.114.93.145:9094'
os.environ['s3AccKey'] = 'public_key'
os.environ['s3SecretKey'] = 'public_secret'
os.environ['s3Host'] = 'http://bdservices-minio.idf-cts.com:9000'
os.environ['entities'] = '{"ora-gg-events": ["hila", "or/events", "True", "False"], "ora-gg-reports": ["hila", "or/reports", "True", "True"]}'