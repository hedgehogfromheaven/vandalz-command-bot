from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    bot_token: str
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    class Config:
        env_file = ".env"

def load_config() -> Settings:
    return Settings()
