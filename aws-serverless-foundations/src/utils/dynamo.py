import os
import boto3

from .constants import USERS_TABLE

client = boto3.resource('dynamodb')

IS_OFFLINE = os.getenv('IS_OFFLINE', False)

if IS_OFFLINE:
    boto3.Session(
        aws_access_key_id='ACCESS_KEY',
        aws_secret_access_key='SECRET_KEY'
    )
    client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = client.Table(USERS_TABLE)
