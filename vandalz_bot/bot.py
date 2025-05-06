import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

# Import our config loader (from config.py)
from config import load_config

# Import routers for commands and other message handling
from handlers.commands import router as command_router
from handlers.echo import router as echo_router

async def main():
    # Load configuration from .env (bot token, etc.)
    config = load_config()

    # Initialize bot with token and default parse mode
    bot = Bot(token=config.bot_token, parse_mode=ParseMode.HTML)

    # Create the main dispatcher to manage handlers
    dp = Dispatcher()

    # Register all command handlers (e.g. /start, /help)
    dp.include_router(command_router)

    # Register echo handler (catches any unmatched text)
    dp.include_router(echo_router)

    # Start polling — this will keep the bot running
    await dp.start_polling(bot)

# This runs the main() function when script is launched directly
if __name__ == "__main__":
    asyncio.run(main())
