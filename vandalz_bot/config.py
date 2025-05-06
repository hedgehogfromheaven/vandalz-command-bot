from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "vandalz"
    DB_USER: str = "vandalz_user"
    DB_PASSWORD: str = "change_this"

    class Config:
        env_file = ".env"

def load_config() -> Settings:
    return Settings()