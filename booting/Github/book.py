from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from HypeVoids import *

@Client.on_message(filters.private
                   &filters.command("github", prefixes="/"))
async def book(_, ydl: Message):
    usrs = ydl.from_user.mention
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "ðã GIÆ¬ÎUB ãð",
          url="https://github.com/HypeVoidSoul")]
        ])
    GBOOK = f"""
ð¦==ð======ð¶======ð==ð¦

Dear,
<b>**{usrs}**</b>

-ê°á´ÊÊá´á´¡ á´á´ ÉªÉ´ É¢Éªá´Êá´Ê.
-á´á´ ê°á´Êá´ á´É´á´ ê±á´á´Ê á´Ê Êá´á´á´ Éªê° Êá´á´ ê°ÉªÉ´á´ á´Êá´á´ á´ê±á´ê°á´ÊÊ

                              
ð¦==ð======ð¶======ð==ð¦                             
"""       
    await ydl.reply_photo(
    "https://telegra.ph/file/888808883d8d70ff35637.jpg",
    reply_markup=joinButton,
    caption=GBOOK
    )
