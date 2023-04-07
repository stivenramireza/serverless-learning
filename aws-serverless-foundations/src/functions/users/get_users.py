import json

from src.utils.dynamo import table


def handler(event, context):
    response = table.scan()

    users = response.get('Items')

    response = {
        'statusCode': 200,
        'body': json.dumps(users)
    }

    return response
