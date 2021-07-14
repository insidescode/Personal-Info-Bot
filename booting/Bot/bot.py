from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from pyrogram import Client, filters
from HypeVoids import *

@Client.on_message(
    filters.private
    &filters.command("bot", prefixes="/"))
async def us(_,ydl: Message):
    BOOT = """
🦋==👓======🕶======👓==🦋   
    
-ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ꜱᴇᴄᴛɪᴏɴ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡɪʟʟ ꜰɪɴᴅ ᴀʟʟ ᴏꜰ @HypeVoidSoul ʙᴏᴛꜱ        
-ᴍᴏʀᴇ ʙᴏᴛꜱ ᴡɪʟʟ ᴋᴇᴇᴘ ᴏɴ ᴄᴏᴍɪɴɢ
-ᴋᴇᴇᴘ ᴀɴ ᴇʏᴇ ᴏɴ ᴄʜᴀɴɴᴇʟ             

🦋==👓======🕶======👓==🦋                                                       
"""
    joinButton = InlineKeyboardMarkup([        
        [InlineKeyboardButton(
          "🔥『 KryoKey Bot』♦️",
          url="https://t.me/KRYOLI_BOT")],
        [InlineKeyboardButton(
          "🔥『 Xeronoid Music Bot 』♦️",
          url="https://t.me/xeronoidbot")],
        [InlineKeyboardButton(
          "🔥『 YouTube Downloader 』♦️",
          url="https://t.me/HVYOUTUBEBOT")],
        [InlineKeyboardButton(
          "🔥『YouTubeMusic Downloader 』♦️",
          url="https://t.me/HVYOUTUBEMUSICBOT")],        
        [InlineKeyboardButton(
          "🔥『 Anime Downloader』♦️",
          url="https://t.me/HVAnimeBot")],
        [InlineKeyboardButton(
          "🔥『 Spotify Downloader』♦️",
          url="https://t.me/HVSPOTIFYBOT")],
        [InlineKeyboardButton(
          "🔥『 Klaw Robot 』♦️",
          url="https://t.me/HVKLAWBOT")],
        [InlineKeyboardButton(
          "🔥『 Image 2 Url 』♦️",
          url="https://t.me/HVIMAGETOURLBOT")],
        [InlineKeyboardButton(
          "🔥『 image 2 Pdf 』♦️",
          url="https://t.me/HVPDFBOT")],
        [InlineKeyboardButton(
          "🔥『 Heroku Usage Bot 』♦️",
          url="https://t.me/HVHEROKUBOT")],
        [InlineKeyboardButton(
          "🔥『 Telegram AFK Bot 』♦️",
          url="https://t.me/HVAFKBOT")]])
    await ydl.reply_animation(
    LINK,
    reply_markup=joinButton,
    caption=BOOT
    )
