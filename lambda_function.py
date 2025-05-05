import boto3
import json
import urllib.parse

rekognition = boto3.client('rekognition', region_name='eu-west-1')

def lambda_handler(event, context):
    print("Event Received:", json.dumps(event))
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        MaxLabels=10
    )

    print("Detected Labels:")
    for label in response['Labels']:
        print(f"{label['Name']} - Confidence: {label['Confidence']:.2f}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Rekognition completed')
    }

