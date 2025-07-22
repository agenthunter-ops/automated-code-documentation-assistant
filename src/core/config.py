from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ACDA"
    APP_VERSION: str = "1.0.0"
    SECRET_KEY: str
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"

    MONGODB_URL: str
    REDIS_URL: str
    DEFAULT_CLONE_PATH: str = "./repos"

    SLACK_BOT_TOKEN: str | None = None
    SLACK_CHANNEL_ID: str | None = None

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
