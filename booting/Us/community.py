from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from pyrogram import Client, filters
from HypeVoids import *

@Client.on_message(
    filters.private
    &filters.command("us",prefixes="/"))
async def us(_,ydl: Message):
    COMMS = """
🦋==👓======🕶======👓==🦋

-ᴡᴇ ʜᴀᴠᴇ ᴀɴ ᴜᴘᴄᴏᴍɪɴɢ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴏꜰ `ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛꜱ` , `ʜᴅ ᴡᴀʟʟᴘᴀᴘᴇʀꜱ` ᴀɴᴅ ᴏꜰ ᴄᴏᴜʀꜱᴇ ᴀ ᴠɪʙʀᴀɴᴛ ᴊᴜꜱᴛ ᴄʜᴀᴛᴛɪɴɢ `ɢʀᴏᴜᴘ`.
-ᴊᴏɪɴ ᴜꜱ ꜰᴏʀ ʀᴀɴᴅᴏᴍ ᴏʀ ʙᴏᴛ-ɪɴꜰᴏ ᴄʜᴀᴛꜱ.      
         
🦋==👓======🕶======👓==🦋                 
"""
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "👓『 𝐆𝐫𝐨𝐮𝐩 』👓",
          url="https://t.me/hypevoids")],
        [InlineKeyboardButton(
          "👓『 𝐖𝐚𝐥𝐥𝐩𝐚𝐩𝐞𝐫𝐬 』👓",
          url="https://t.me/vrtxwalls")],
        [InlineKeyboardButton(
          "👓『 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 』👓",
          url="https://t.me/hypevoidlab")],
        ])
    await ydl.reply_animation(
    LINK,
    reply_markup=joinButton,
    caption=COMMS
    )
