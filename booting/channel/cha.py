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
          "👓『 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 』👓",
          url="https://github.com/HypeVoidLab")]
        ])
    GBOOK = f"""
🦋==👓======🕶======👓==🦋

Dear,
<b>**{usrs}**</b>

『  ∆   ʜᴜʙ ᴏꜰ ʙᴏᴛꜱ ᴡɪᴛʜ ᴇᴍᴏᴛɪᴏɴ  ∆ 』

The hub of awsome Telegram Bots.
Keep eye on us to get to use new and interesting bots.

                              
🦋==👓======🕶======👓==🦋                             
"""       
    await ydl.reply_photo(
    "https://telegra.ph/file/888808883d8d70ff35637.jpg",
    reply_markup=joinButton,
    caption=GBOOK
    )
