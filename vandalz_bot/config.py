from dataclasses import dataclass
import os

@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")

settings = Settings()