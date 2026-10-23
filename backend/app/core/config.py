from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str = "development"
    LOG_LEVEL: str = "INFO"

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/hetupr"
    REDIS_URL: str = "redis://localhost:6379/0"

    GITHUB_APP_ID: str = ""
    GITHUB_WEBHOOK_SECRET: str = ""
    GITHUB_PRIVATE_KEY_PATH: str = "./certs/github-private-key.pem"

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
