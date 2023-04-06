import time
import os
import random

global_random_value = random.random()


def cold_start_basics(event, context):
    local_random_value = random.random()
    print(local_random_value)
    print(global_random_value)


def simple_types(event, context):
    print(event)
    return event


def list_types(event, context):
    print(event)
    student_scores = {"John": 100, "Bob": 90, "Stiven": 100}
    scores = []
    for name in event:
        scores.append(student_scores[name])
    return scores


def dict_types(event, context):
    john_scores = event["John"]
    for score in john_scores:
        print(score)
    return event


def lambda_handler(event, context):
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:", context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    time.sleep(4)
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())
    print(os.getenv("REST_API_URL"))
    print(os.getenv("DB_NAME"))
