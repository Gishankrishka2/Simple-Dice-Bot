from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
import random
from config import *

Client = Client(
    "Memehub Bot",
    bot_token= BOT_TOKEN,
    api_id= API_ID,
    api_hash= API_HASH,
)

DICE = ["1️⃣",
       "2️⃣",
       "3️⃣",
       "4️⃣", 
       "5️⃣", 
       "6️⃣", 
       "7️⃣", 
       "8️⃣", 
       "9️⃣", 
       "🔟", 
       "1️⃣1️⃣", 
       "1️⃣2️⃣", 
       "1️⃣3️⃣", 
       "1️⃣4️⃣", 
       "1️⃣5️⃣", 
       "1️⃣6️⃣", 
       "1️⃣7️⃣", 
       "1️⃣8️⃣", 
       "1️⃣9️⃣", 
       "2️⃣0️⃣"              
       ]

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="1868693153")
                 ],
                 [
                 InlineKeyboardButton("┊𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』", url="https://t.me/AlphaTm_Botz"),
                 InlineKeyboardButton("Support - ┊𝙰𝙻𝙿𝙷𝙰 Botz Chat ", url="https://t.me/AlphaTm_Botz_chat")
                 ]]
                  )

start_menu = ReplyKeyboardMarkup(
      [
            ["Roll"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )


@Client.on_message(filters.command("start"))
async def startprivate(bot, message):
    await bot.send_sticker(message.chat.id, "CAADBQADRQYAAq3nEFcH9wWixTzJyQI", reply_markup=start_menu)
    await bot.send_message(message.chat.id, '''🎲𝗣𝗮𝗶 𝗦𝗵𝗼 𝗶𝘀 𝗮 𝗳𝗼𝗿𝗺𝗲𝗿𝗹𝘆-𝗳𝗶𝗰𝘁𝗶𝗼𝗻𝗮𝗹 𝗯𝗼𝗮𝗿𝗱 𝗴𝗮𝗺𝗲 𝘀𝗲𝗲𝗻 𝗶𝗻 𝗔𝘃𝗮𝘁𝗮𝗿: 𝗧𝗵𝗲 𝗟𝗮𝘀𝘁 𝗔𝗶𝗿𝗯𝗲𝗻𝗱𝗲𝗿. 
🎲𝗔𝗹𝗹 𝘁𝗵𝗮𝘁'𝘀 𝘀𝗵𝗼𝘄𝗻 𝗶𝗻 𝘁𝗵𝗲 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝘀 𝘁𝗵𝗲 𝗯𝗼𝗮𝗿𝗱 𝗮𝗻𝗱 𝗮 𝗳𝗲𝘄 𝗼𝗳 𝘁𝗵𝗲 𝗴𝗮𝗺𝗲 𝗽𝗶𝗲𝗰𝗲𝘀. 
🎲𝗡𝗼 𝗿𝘂𝗹𝗲𝘀 𝗮𝗿𝗲 𝗴𝗶𝘃𝗲𝗻. 𝗧𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗿𝗲𝗮𝗹𝗹𝘆 𝘂𝘀𝗲𝗱 𝘁𝗼 𝗯𝗲 𝗮 𝟮𝟬 𝘀𝗶𝗱𝗲 𝗱𝗶𝗰𝗲 (𝗱𝟮𝟬).''', reply_markup=START_BUTTON)
  
@Client.on_message(filters.regex(pattern="Roll"))   
async def dice(bot, message):
     await bot.send_message(message.chat.id, random.choice(DICE))



print(" Deployed Successfully !")        
Client.run()
