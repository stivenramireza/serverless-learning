import os
import boto3

dynamo_db = boto3.resource("dynamodb")
CUSTOMERS_TABLE = os.getenv("CUSTOMERS_TABLE")
