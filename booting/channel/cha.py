from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from HypeVoids import *

@Client.on_message(
filters.private
&filters.command("channel",
prefixes="/"))
async def book(_, ydl: Message):
    usrs = ydl.from_user.mention
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "๐ใ ๐๐ก๐๐ง๐ง๐๐ฅ ใ๐",
          url="https://t.me/HypeVoidLab")]
        ])
    GBOOK = f"""
๐ฆ==๐======๐ถ======๐==๐ฆ

Dear,
<b>**{usrs}**</b>

ใ  โ   สแดส แด๊ฐ สแดแด๊ฑ แดกษชแดส แดแดแดแดษชแดษด  โ ใ

The hub of awsome Telegram Bots.
Keep eye on us to get to use new and interesting bots.

                              
๐ฆ==๐======๐ถ======๐==๐ฆ                             
"""       
    await ydl.reply_photo(
    "https://telegra.ph/file/9f1ac4173a2dd520d67b4.jpg",
    reply_markup=joinButton,
    caption=GBOOK
    )
