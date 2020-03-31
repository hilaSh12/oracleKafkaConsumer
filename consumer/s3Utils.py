import boto3
import uuid

def createS3Connection(s3AccKey, s3SecretKey, s3Host):
    s3 = boto3.resource('s3', aws_access_key_id=s3AccKey, aws_secret_access_key=s3SecretKey, endpoint_url=s3Host)
    return s3

def putMessageInS3(s3conn, destBucket, message, path):
    s3conn.Object(destBucket, path).put(Body=str(message))
    print("put message on %path", path)

def setPathToFile(directory, message, isYear, isMonth):
    path = directory + "/"
    if 'je_operation_date' in message:
        date = message['je_operation_date']
        path += date[:4] + "/" if isYear else ""
        path += date[5:7] + "/" if isMonth else ""
    path += str(uuid.uuid1())
    return path
