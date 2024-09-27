import os
import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
import pyromod.listen  # Import pyromod listen

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.ERROR)

# Initialize the bot client
plugins = dict(root="HEROKUHELP/plugins")
app = Client(
    "HEROKUHELP",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    
)


