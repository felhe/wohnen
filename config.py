import logging
import os

loglevel = os.environ['LOG_LEVEL'] if 'LOG_LEVEL' in os.environ else 'INFO'

logging.basicConfig(level=loglevel)

jsonfile = "./wohnen.json"

# Set up logger for config
logger = logging.getLogger(__name__)

bot_token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = os.environ['TELEGRAM_CHAT_ID']
channel_id = os.environ['TELEGRAM_CHANNEL_ID']

# Log environment variables (without exposing the token)
logger.info(f"Telegram bot configured - Chat ID: {chat_id}, Channel ID: {channel_id}")

# set search parameters
min_rooms = 1
max_rooms = 3
# max rent or 700 as default
max_rent = os.environ['MAX_RENT'] if 'MAX_RENT' in os.environ else 700
logger.info(f"Max rent configured: {max_rent}")

bez = [
    "01_00",
    "02_00",
    "09_00",
    "11_00"
]

# 0 = no wbs
# 1 = only wbs
# 2 = doesn't matter
# parse as int
wbs = int(os.environ['WBS']) if 'WBS' in os.environ else 2
logger.info(f"WBS setting: {wbs}")
