import json

from ...utils.dynamo import table

def handler(event, context):
    user_id = event.get('pathParameters').get('id')
    result = table.delete_item(Key={
        'pk': user_id
    })

    body = json.dumps({
        'message': f'User {user_id} deleted'
    })

    response = {
        'statusCode': result.get('ResponseMetadata').get('HTTPStatusCode'),
        'body': body
    }

    return response
