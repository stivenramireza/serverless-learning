import os
import boto3

dynamo_db = boto3.resource("dynamodb")
ORDERS_TABLE = os.getenv("ORDERS_TABLE")
