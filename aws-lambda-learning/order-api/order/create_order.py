import json

from order.app import dynamo_db, ORDERS_TABLE


def lambda_handler(event, context):
    order = json.loads(event.get("body"))

    table = dynamo_db.Table(ORDERS_TABLE)
    response = table.put_item(TableName=ORDERS_TABLE, Item=order)
    print(response)

    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps({"message": "Order has been created successfully"}),
    }
