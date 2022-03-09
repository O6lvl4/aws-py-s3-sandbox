import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('motodera.s3-python-sandbox.development.any')
    bucket.upload_file('fuga.txt', 'fuga.txt')
    print(bucket)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
