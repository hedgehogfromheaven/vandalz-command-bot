import os
from dotenv import dotenv_values

secrets = {
    **dotenv_values("../vandalz.env"),
    **os.environ
}

BOT_TOKEN = secrets["BOT_TOKEN"]

DB_CONFIG = {
    "host": secrets["DB_HOST"],
    "port": int(secrets["DB_PORT"]),
    "user": secrets["DB_USER"],
    "password": secrets["DB_PASS"],
    "database": secrets["DB_NAME"],
}
