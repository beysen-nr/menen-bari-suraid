from telethon import events
from infrastructure.telegram_service import bot

from infrastructure.telegram_service import register_handler, run_bot
from adapters.telegram_adapter import message_handler

if __name__ == "__main__":
    register_handler(message_handler)
    run_bot()
