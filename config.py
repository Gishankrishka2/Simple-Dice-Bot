import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
import json
import requests
import wget

BOT_TOKEN = os.getenv("BOT_TOKEN", "5494219369:AAFk5iMvpwjvWi3MoKXcNYQuBHa5wJ-_qMY")  # from @botfather
API_ID = int(os.getenv("API_ID", "8838171"))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH", "0587408d4f7d9301f5295840b0f3b494")  # from https://my.telegram.org/apps

