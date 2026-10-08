from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    ha_base_url: str = "http://homeassistant.local:8123"
    ha_token: SecretStr
    database_url: str


settings = Settings()
