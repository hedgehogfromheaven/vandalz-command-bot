# vandalz_bot/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    vandalz_token: str  # новое имя переменной

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

def load_config():
    return Settings()
