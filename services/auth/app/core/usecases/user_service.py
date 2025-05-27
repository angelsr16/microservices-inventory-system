from datetime import datetime, timezone
from dataclasses import asdict
from app.core.entities.user import User
from app.interfaces.user_repository import IUserRepository


class UserService:
    def __init__(self, repo: IUserRepository, hasher, token_creator):
        self.repo = repo
        self.hash_password = hasher
        self.create_token = token_creator

    def register(self, username: str, password: str) -> str:
        if self.repo.get_by_username(username):
            raise ValueError("Username already exists")

        hashed = self.hash_password(password)
        now_utc = datetime.now(timezone.utc)
        user = User(
            username=username,
            password_hash=hashed,
            created_at=now_utc,
        )
        self.repo.save(user)

        return self.create_token(asdict(user))

    def login(self, username: str, password: str, verifier) -> str:
        user = self.repo.get_by_username(username)
        if not user or not verifier(password, user.password_hash):
            raise ValueError("Invalid credentials")
        print(user)
        return self.create_token(asdict(user))
