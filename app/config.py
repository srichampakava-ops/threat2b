from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Values come from environment variables or a local .env file.
    app_name: str = "ThreatBridge API"
    app_version: str = "0.1.0"
    environment: str = "development"  # "development" or "production"

    # Comma-separated list of frontend addresses allowed to call this API.
    allowed_origins: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def origins_list(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]


settings = Settings()