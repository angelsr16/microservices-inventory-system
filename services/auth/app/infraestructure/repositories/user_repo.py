from typing import Optional
import boto3
from app.infraestructure.db.dynamodb import get_dynamodb_resource
from app.core.entities.user import User
from app.interfaces.user_repository import IUserRepository
from datetime import datetime


class DynamoUserRepository(IUserRepository):
    def __init__(self):
        self.table = get_dynamodb_resource().Table("users")

    def get_by_username(self, username: str) -> Optional[User]:
        response = self.table.get_item(Key={"username": username})
        item = response.get("Item")
        if item:
            return User(
                username=item["username"],
                password_hash=item["password_hash"],
                created_at=datetime.fromisoformat(item["created_at"]),
            )

        return None

    def save(self, user: User) -> None:
        created_at_str = user.created_at.isoformat()

        self.table.put_item(
            Item={
                "username": user.username,
                "password_hash": user.password_hash,
                "created_at": created_at_str,
            }
        )
