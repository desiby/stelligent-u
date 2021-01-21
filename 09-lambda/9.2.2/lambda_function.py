import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('s3log')

def lambda_handler(event, context):
    print("receiving event..")
    print(json.dumps(event))
    objectKey = json.dumps(event["detail"]["requestParameters"]["key"])
    table.put_item (
         Item={
            "id": str(uuid.uuid4()),
            "object": objectKey
        }
    )
    return {
        'statusCode': 200,
        'message': "row inserted!"
    }