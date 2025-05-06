# vandalz_bot/config.py

from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    vandalz_token: str = Field(..., env='VANDALZ_TOKEN')

def load_config():
    return Settings()
