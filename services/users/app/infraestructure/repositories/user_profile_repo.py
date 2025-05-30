import datetime
from typing import Optional
from core.entities.user_profile import UserProfile
from infraestructure.db.dynamodb import get_dynamodb_resource
from interfaces.user_profile_repository import IUserProfileRepository

from datetime import datetime


class DynamoUserProfileRepository(IUserProfileRepository):
    def __init__(self):
        self.table = get_dynamodb_resource().Table("users_profiles")

    def get_by_username(self, username: str) -> Optional[UserProfile]:
        response = self.table.get_item(Key={"username": username})
        item = response.get("Item")

        if item:
            return UserProfile(
                username=item["username"],
                firstName=item["firstName"],
                lastName=item["lastName"],
                roles=item["roles"],
                created_at=datetime.isoformat(item["created_at"]),
                updated_at=datetime.isoformat(item["updated_at"]),
            )

    def save(self, user_profile: UserProfile) -> None:
        created_at_str = user_profile.created_at.isoformat()
        updated_at_str = user_profile.updated_at.isoformat()

        self.table.put_item(
            Item={
                "username": user_profile.username,
                "firstName": user_profile.firstName,
                "lastName": user_profile.lastName,
                "roles": user_profile.roles,
                "created_at": created_at_str,
                "updated_at": updated_at_str,
            }
        )
