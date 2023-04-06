from logger import logger


def lambda_handler(event: any, context: object) -> None:
    message = event["Records"][0]["Sns"]["Message"]
    logger.info(f"Result: {message}")
