import json

from app import dynamo_db, CUSTOMERS_TABLE


def lambda_handler(event, context):
    order = json.loads(event.get("body"))

    table = dynamo_db.Table(CUSTOMERS_TABLE)
    response = table.put_item(TableName=CUSTOMERS_TABLE, Item=order)
    print(response)

    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps({"message": "Customer has been created successfully"}),
    }
