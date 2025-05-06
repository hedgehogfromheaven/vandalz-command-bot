import os

class Settings:
    def __init__(self):
        self.token = os.getenv("BOT_TOKEN", "no-token-found")

def load_config():
    return Settings()
