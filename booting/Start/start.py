from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from HypeVoids import *

@Client.on_message(filters.private
                   &filters.command("start", prefixes="/"))
async def start(_, ydl: Message):
    usrs = ydl.from_user.mention
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "πγHypeVoidSoul ?γπ",
          url="https://t.me/HypeVoidSoul")]
        ])
    START = f"""
π¦==π======πΆ======π==π¦

πDear,
    Sir,Ma'am  
        <b>**{usrs}**</b>

**πΏπππππ πππππ πππππ  ππππππππ πππ ππ’ πππ**
-prΔΕΕ /bot

-prΔΕΕ /us
    -or-
-prΔΕΕ /channel

-prΔΕΕ /github
-prΔΕΕ /walls

                              
π¦==π======πΆ======π==π¦                             
"""       
    await ydl.reply_animation(
    LINK,
    reply_markup=joinButton,
    caption=START
    )
