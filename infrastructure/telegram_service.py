from telethon import TelegramClient, events
from config import settings

bot = TelegramClient(
    "menenbarisuraidybot",
    settings.API_ID,
    settings.API_HASH
).start(bot_token=settings.BOT_TOKEN)



def register_handler(handler):
    """Registers a message handler from adapter layer."""
    bot.add_event_handler(handler, events.NewMessage)

def run_bot():
    print("🤖 Bot is running...")
    bot.run_until_disconnected()
