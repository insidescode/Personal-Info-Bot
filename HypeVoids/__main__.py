from pyrogram import Client
from pyrogram.methods.utilities import idle
from booting import *

boot = Client(
    KryoTM,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=8
)
boot.start()
print('🍁🎷一═デ︻ Wê Ärê H¥þêVðïÐ§ ︻デ═一')
print('ONLINE🍁🎷')
idle()
boot.stop()
print('🍁⚰️一═デ︻ Wê Ärê H¥þêVðïÐ§ ︻デ═一')
print('OFFLINE ⚰️🍁')