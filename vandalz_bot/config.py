import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}