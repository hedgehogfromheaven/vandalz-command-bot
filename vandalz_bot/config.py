from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    bot_token: str

    class Config:
        env_file = ".env"

def load_config():
    return Settings()
