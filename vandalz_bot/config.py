from pydantic import BaseSettings

class Settings(BaseSettings):
    bot_token: str

    class Config:
        env_file = ".env"

def load_config() -> Settings:
    return Settings()
