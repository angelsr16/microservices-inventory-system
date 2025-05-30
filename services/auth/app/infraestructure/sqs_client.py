import boto3
import json
import core_settings


class SQSClient:
    def __init__(self, queue_url: str = None):
        self.queue_url = queue_url or core_settings.SQS_USER_REGISTERED_URL
        self.client = boto3.client(
            "sqs",
            aws_access_key_id=core_settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=core_settings.AWS_SECRET_ACCESS_KEY,
            region_name=core_settings.AWS_REGION,
        )

    def send_message(self, message: dict):
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(message),
        )
        print(response)
        return response
