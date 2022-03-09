import json
import boto3
from boto3_type_annotations import s3


BUCKET_NAME = "motodera.s3-python-sandbox.development.any"

def upload_to_s3(bucket_name: str, upload_file_path: str, s3_key_name: str):
    s3Resource: s3.ServiceResource = boto3.resource('s3')
    bucket: s3.Bucket = s3Resource.Bucket(bucket_name)
    bucket.upload_file(upload_file_path, s3_key_name)

def download_at_s3(bucket_name: str, s3_key_name: str, download_file_path: str):
    s3Resource: s3.ServiceResource = boto3.resource('s3')
    bucket = s3Resource.Bucket(bucket_name)
    bucket.download_file(s3_key_name, download_file_path)

def lambda_handler(event, context):
    upload_to_s3(BUCKET_NAME, 'fuga.txt', 'example/sample.txt')
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

download_at_s3(BUCKET_NAME, "example/sample.txt", "test.txt")
