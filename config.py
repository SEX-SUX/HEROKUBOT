
import re

from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID", "")

API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

OWNER_ID = getenv("OWNER_ID", "7373125778")
    
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SEX-SUX/HEROKUBOT")
