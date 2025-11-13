"""Configuration management using environment variables."""
import os
from functools import lru_cache


class Settings:
    # Database settings
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_USER: str = os.getenv("DB_USER", "appuser")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "apppass")
    DB_NAME: str = os.getenv("DB_NAME", "appdb")

    @property
    def DATABASE_URL(self) -> str:
        """Construct database URL from components."""
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Application settings
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
