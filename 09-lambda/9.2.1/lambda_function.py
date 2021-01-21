import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user')

def lambda_handler(event, context):
    userid = event['id']
    username = event['name']
    
    table.put_item(
       Item={
           "id": userid,
           "name": username
       } 
    )
    return {
        'statusCode': 200,
        'message': "row inserted!"
    }