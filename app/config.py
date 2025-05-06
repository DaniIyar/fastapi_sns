from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_url: Optional[str] = None
    database_hostname: Optional[str] = None
    database_port: Optional[str] = None
    database_username: Optional[str] = None
    database_password: Optional[str] = None
    database_name: Optional[str] = None
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"  # Use a .env file for local development

    def get_database_url(self) -> str:
        # Returns the database URL.
        # Otherwise, it constructs the URL using individual settings for local use.

        if self.database_url:
            return self.database_url
        return (
            f"postgresql+psycopg://{self.database_username}:"
            f"{self.database_password}@{self.database_hostname}:"
            f"{self.database_port}/{self.database_name}"
        )

settings = Settings()
