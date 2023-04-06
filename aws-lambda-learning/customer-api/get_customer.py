import simplejson as json
from boto3.dynamodb.conditions import Key

from app import dynamo_db, CUSTOMERS_TABLE


def lambda_handler(event, context):
    table = dynamo_db.Table(CUSTOMERS_TABLE)

    order_id = int(event.get("pathParameters").get("id"))
    response = table.query(KeyConditionExpression=Key("id").eq(order_id))
    print(response)

    return {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(response.get("Items")),
    }
