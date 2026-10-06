from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    database_url: str
    secret_key: SecretStr
    access_token_expire_minutes: int = 120
    gemini_api_key: SecretStr | None = None
    gemini_model: str = "gemini-2.5-flash"

settings = Settings()
