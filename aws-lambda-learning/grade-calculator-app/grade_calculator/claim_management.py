from logger import logger


def lambda_handler(event: any, context: object) -> None:
    for event in event["Records"]:
        logger.info(event.get("body"))
