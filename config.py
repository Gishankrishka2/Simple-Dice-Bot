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

BOT_TOKEN = os.getenv("BOT_TOKEN", "")  # from @botfather
API_ID = int(os.getenv("API_ID", ""))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH", "")  # from https://my.telegram.org/apps

