import boto3
import core_settings


def get_dynamodb_resource():
    if core_settings.ENV == "development":
        return boto3.resource(
            "dynamodb",
            aws_access_key_id=core_settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=core_settings.AWS_SECRET_ACCESS_KEY,
            region_name=core_settings.AWS_REGION,
        )
    else:
        return boto3.resource("dynamodb")
