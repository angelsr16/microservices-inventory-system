import json
from fastapi import FastAPI
from mangum import Mangum

from api.dependencies.user_profile_service import create_user_profile_service
from schemas.user_profile_schema import UserProfileRegister

app = FastAPI()

# AWS LAMBDA HANDLER
asgi_handler = Mangum(app)


@app.get("/users")
async def root():
    return {"msg": "Hello from users service"}


user_profile_service = create_user_profile_service()


def handler(event, context):
    # Check for API Gateway v1 or v2 (HTTP)
    if "httpMethod" in event or (
        event.get("version") == "2.0" and "requestContext" in event
    ):
        return asgi_handler(event, context)

    # SQS event
    if "Records" in event and event["Records"][0]["eventSource"] == "aws:sqs":
        for record in event["Records"]:
            try:
                body = json.loads(record["body"])
                user_profile_data = UserProfileRegister(**body)
                user_profile_service.register(user_profile_data)
                print(f"Registered user from SQS: {user_profile_data.username}")
            except Exception as e:
                print(f"Error processing SQS message: {e}")
        return {"statusCode": 200, "body": "Processed SQS message"}

    return {"statusCode": 400, "body": "Unknown event source"}
