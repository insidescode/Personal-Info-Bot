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
          "👓『 GIƬΉUB 』👓",
          url="https://github.com/HypeVoidSoul")]
        ])
    GBOOK = f"""
🦋==👓======🕶======👓==🦋

Dear,
<b>**{usrs}**</b>

-ꜰᴏʟʟᴏᴡ ᴍᴇ ɪɴ ɢɪᴛʜᴜʙ.
-ᴅᴏ ꜰᴏʀᴋ ᴀɴᴅ ꜱᴛᴀʀ ᴍʏ ʀᴇᴘᴏ ɪꜰ ʏᴏᴜ ꜰɪɴᴅ ᴛʜᴇᴍ ᴜꜱᴇꜰᴜʟʟ

                              
🦋==👓======🕶======👓==🦋                             
"""       
    await ydl.reply_photo(
    "https://telegra.ph/file/888808883d8d70ff35637.jpg",
    reply_markup=joinButton,
    caption=GBOOK
    )
