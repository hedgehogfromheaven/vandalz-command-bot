import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
