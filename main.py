from pyrogram import Client, filters
import random
from flask import Flask
from threading import Thread
import os

# Flask server for UptimeRobot
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti! ✅"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Start Flask in background thread
Thread(target=run_flask).start()

# Bot uchun ma'lumotlar
API_ID = 24410919
API_HASH = "11a3a20ee4f9e851e35412b0a2eedb3a"
BOT_TOKEN = "7761148498:AAGbFdR2gda_1ZPMEtifoW4qv186Cmg6tFI"

# Pyrogram Client yaratish
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# So'z va javoblar ro'yxati
javoblar = {
    "salom": [
        "Salom! Qanday ketyapti? 😊",
        "Assalomu alaykum! 👋", 
        "Salom, do'stim!",
        "Yaxshi kun!",
        "Salom! Ishlaringizni qilib yurganingizni ko'rib turibman!",
        "Salom! Yangi kunni qanday kutyapsiz?"
    ],
    # ... (qolgan javoblar ro'yxati o'zgarmagan holda qoldiriladi)
    # Sizning mavjud javoblar ro'yxatingiz shu yerda bo'ladi
}

# Botni start bosilganda o'zini tanishtirish
@bot.on_message(filters.command("start") & filters.private)
def start(client, message):
    message.reply_text("Assalomu alaykum! Men Sinfdoshlar 2009 Botiman. Qanday yordam bera olaman! 😊")

# Xabarlarga javob berish 
@bot.on_message(filters.text)
def javob_ber(client, message):
    matn = message.text.lower().strip()
    for soz, javob in javoblar.items():
        if soz in matn:
            message.reply_text(random.choice(javob))
            return

    message.reply_text("Bu haqida nima deb o'ylaysiz? 🤔")

# Botni ishga tushirish
bot.run()
