import asyncio
import logging
from asyncio import Queue

from telegram import Bot
from telegram.ext import Updater

import config
from apartment import Apartment

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def send_apartment(apartment: Apartment):
    bot = Bot(token=config.bot_token)
    # formatted message, add link if available
    text = f"""
{'❗ WBS erforderlich' if 'wbs' in apartment and apartment['wbs'] == 'erforderlich' else ''}
📍 {apartment['addr']}
💶 {f"{apartment['price']:.2f}".replace('.', ',')} € kalt
📐 {apartment['sqm']} m²
🛏 {apartment['rooms']} Zimmer
📅 {apartment['timeframe']}
🏗️ Baujahr {apartment['year']}
🛗 Etage {apartment['floor']}
{'🔗 ' + apartment['link'] if 'link' in apartment else ''}
    """.strip()

    # start polling for updates for max 30 seconds total
    updates = Queue()
    updater: Updater = Updater(bot=bot, update_queue=updates)
    await updater.initialize()
    await updater.start_polling(allowed_updates=["message"], timeout=10)

    # send image if available
    if 'image' in apartment:
        message = await bot.send_photo(chat_id=config.channel_id, photo=apartment['image'], caption=text)
    else:
        message = await bot.send_message(chat_id=config.channel_id, text=text)

    # wait for updates until certain message is received
    # stop polling after 30 seconds
    while updater.running:
        try:
            update = await asyncio.wait_for(updates.get(), timeout=30)
            if update.message.forward_from_message_id == message.message_id:
                await bot.send_location(chat_id=config.chat_id, reply_to_message_id=update.message.message_id,
                                        latitude=apartment['coords'][0], longitude=apartment['coords'][1])
                await updater.stop()
        except asyncio.exceptions.TimeoutError:
            await updater.stop()
