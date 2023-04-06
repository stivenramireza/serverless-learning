import json
from typing import Dict


def lambda_handler(event: any, context: object) -> Dict[str, any]:
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "hello world"}),
    }
