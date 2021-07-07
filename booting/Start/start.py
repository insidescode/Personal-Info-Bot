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
          "👓『HypeVoidSoul ?』👓",
          url="https://t.me/HypeVoidSoul")]
        ])
    START = f"""
🦋==👓======🕶======👓==🦋

🎈Dear,
    Sir,Ma'am  
        <b>**{usrs}**</b>

**𝙿𝚕𝚎𝚊𝚜𝚎 𝚌𝚕𝚒𝚌𝚔 𝚋𝚎𝚕𝚘𝚠 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚘𝚗𝚎 𝚋𝚢 𝚘𝚗𝚎**
-prēŞŞ /bot

-prēŞŞ /us
    -or-
-prēŞŞ /channel

-prēŞŞ /github
-prēŞŞ /walls

                              
🦋==👓======🕶======👓==🦋                             
"""       
    await ydl.reply_photo(
    LINK,
    reply_markup=joinButton,
    caption=START
    )