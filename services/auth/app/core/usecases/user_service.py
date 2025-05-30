from datetime import datetime, timezone
from dataclasses import asdict
from schemas.user_schema import UserRegister
from infraestructure.sqs_client import SQSClient
from core.entities.user import User
from interfaces.user_repository import IUserRepository


class UserService:
    def __init__(
        self,
        repo: IUserRepository,
        hasher,
        token_creator,
        verifier,
        sqs_client: SQSClient,
    ):
        self.repo = repo
        self.hash_password = hasher
        self.create_token = token_creator
        self.verifier = verifier
        self.sqs_client = sqs_client

    def register(self, user_register: UserRegister) -> str:
        if self.repo.get_by_username(user_register.username):
            raise ValueError("Username already exists")

        hashed = self.hash_password(user_register.password)
        now_utc = datetime.now(timezone.utc)
        user = User(
            username=user_register.username,
            password_hash=hashed,
            created_at=now_utc,
        )
        self.repo.save(user)

        self.sqs_client.send_message(
            {
                "username": user_register.username,
                "firstName": user_register.firstName,
                "lastName": user_register.lastName,
                "roles": user_register.roles,
            }
        )

        return self.create_token(asdict(user))

    def login(self, username: str, password: str) -> str:
        user = self.repo.get_by_username(username)
        if not user or not self.verifier(password, user.password_hash):
            raise ValueError("Invalid credentials")
        return self.create_token(asdict(user))
