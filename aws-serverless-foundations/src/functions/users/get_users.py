import json
from decimal import Decimal

from src.utils.dynamo import table

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def handler(event, context):
    response = table.scan()

    users = response.get('Items')

    response = {
        'statusCode': 200,
        'body': json.dumps(users, cls=DecimalEncoder)
    }

    return response
