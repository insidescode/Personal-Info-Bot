from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from pyrogram import Client, filters
from HypeVoids import *

@Client.on_message(
    filters.private
    &filters.command("walls", prefixes="/"))
async def wallpapers(_,ydl: Message):
    WALI = """
🦋==👓======🕶======👓==🦋

-ᴏɴᴇ ᴘʟᴀᴄᴇ ꜰᴏʀ ʜɪɢʜᴛᴇꜱᴛ Qᴜᴀʟɪᴛʏ ᴡᴀʟʟᴘᴀᴘᴇʀꜱ.
-ᴊᴏɪɴ!
                
🦋==👓======🕶======👓==🦋                         
"""
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "👓『 𝐖𝐚𝐥𝐥𝐩𝐚𝐩𝐞𝐫𝐬 』👓",
          url="https://t.me/vrtxwalls")]
        ])
    await ydl.reply_animation(
    LINK,
    reply_markup=joinButton,
    caption=WALI
    )
