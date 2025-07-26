import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def lambda_handler(event, context):
    method = event['requestContext']['http']['method']

    if method == 'POST':
        data = json.loads(event['body'])
        item = {'id': str(uuid.uuid4()), **data}
        table.put_item(Item=item)
        return {"statusCode": 201, "body": json.dumps(item)}

    elif method == 'GET':
        items = table.scan().get('Items', [])
        return {"statusCode": 200, "body": json.dumps(items)}

    else:
        return {"statusCode": 405, "body": json.dumps({'error': 'Method Not Allowed'})}
