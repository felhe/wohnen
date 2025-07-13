import os
from logging import DEBUG, INFO, WARNING, ERROR

jsonfile = "./wohnen.json"
loglevel = INFO

bot_token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = os.environ['TELEGRAM_CHAT_ID']
channel_id = os.environ['TELEGRAM_CHANNEL_ID']

# set search parameters
min_rooms = 1
max_rooms = 3
# max rent or 700 as default
max_rent = os.environ['MAX_RENT'] if 'MAX_RENT' in os.environ else 700
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
