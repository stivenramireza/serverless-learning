import os
import json
import boto3
from typing import Dict

from logger import logger


s3_client = boto3.client("s3")
sns_client = boto3.client("sns")
sns_topic = os.getenv("GRADE_CALCULATOR_TOPIC")


def calculate_grade(test_score: Dict[str, any]) -> str:
    if test_score > 70:
        return "A"
    elif 60 <= test_score <= 70:
        return "B"
    elif test_score < 60:
        return "C"
    else:
        return "No assigned"


def lambda_handler(event: any, context: object) -> None:
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_key = event["Records"][0]["s3"]["object"]["key"]
    logger.info(f"Reading {file_key} from {bucket_name}")
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_content = obj.get("Body").read().decode("utf-8")

    score_events = json.loads(file_content)
    for event in score_events:
        logger.info("Messaging being published")
        logger.info(event)
        # Calculate the graded based on their test_score
        test_score = event.get("testScore")
        calculated_grade = calculate_grade(test_score)
        event.update({"grade": calculated_grade})

        # Publish events to SNS topic
        sns_client.publish(
            TopicArn=sns_topic,
            Message=json.dumps({"default": json.dumps(event)}),
            MessageStructure="json",
        )
