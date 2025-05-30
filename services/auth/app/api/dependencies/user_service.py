from fastapi import Depends
from infraestructure.repositories.user_repo import DynamoUserRepository
from infraestructure.sqs_client import SQSClient
from core.usecases.user_service import UserService
from services.auth import hash_password, verify_password
from services.jwt import create_access_token


def get_sqs_client():
    return SQSClient()


def get_user_repository():
    return DynamoUserRepository()


def get_user_service(
    repo=Depends(get_user_repository), sqs_client=Depends(get_sqs_client)
):
    return UserService(
        repo=repo,
        hasher=hash_password,
        token_creator=create_access_token,
        verifier=verify_password,
        sqs_client=sqs_client,
    )
