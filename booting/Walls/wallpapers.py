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
๐ฆ==๐======๐ถ======๐==๐ฆ

-แดษดแด แดสแดแดแด ๊ฐแดส สษชษขสแดแด๊ฑแด Qแดแดสษชแดส แดกแดสสแดแดแดแดส๊ฑ.
-แดแดษชษด!
                
๐ฆ==๐======๐ถ======๐==๐ฆ                         
"""
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "๐ใ ๐๐๐ฅ๐ฅ๐ฉ๐๐ฉ๐๐ซ๐ฌ ใ๐",
          url="https://t.me/vrtxwalls")]
        ])
    await ydl.reply_animation(
    LINK,
    reply_markup=joinButton,
    caption=WALI
    )
