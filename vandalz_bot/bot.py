from aiogram import Bot, Dispatcher
from config import load_config

config = load_config()
bot = Bot(token=config.bot_token)
dp = Dispatcher()
