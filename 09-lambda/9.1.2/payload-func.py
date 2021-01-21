import json

def lambda_handler(event, context):
    fn = event['first_name']
    ln = event['last_name'] 
    return { 
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'first_name': fn,
            'last_name':ln
        })
    }