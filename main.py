import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.exceptions import TelegramAPIError
from dotenv import load_dotenv

from handlers.routes import router
from middleware.rate_limit import RateLimitMiddleware


# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")


# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def main() -> None:
    # Initialize bot and dispatcher
    bot = Bot(
        token=TOKEN,
        properties=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher(storage=MemoryStorage())

    dp.message.middleware(RateLimitMiddleware()) # Add rate limiting middleware to the dispatcher

    dp.include_router(router) # Register handlers

    await bot.set_my_commands([
        BotCommand(command="translate", description="Translate text to another language")
    ])

    try:
        await dp.start_polling(bot) # Start polling
    except TelegramAPIError as e:
        logger.error(f"Error occurred while starting polling: {e}") # Log the error if polling fails
    finally:
        await bot.session.close() # Close the bot session on shutdown

if __name__ == "__main__":
    asyncio.run(main())