from pyrogram import Client, filters
import random
from flask import Flask
from threading import Thread
import os
import time
import logging

# Loglarni sozlash (bot ishlashi haqida ma'lumot saqlash)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Flask dasturini yaratamiz (server holatini tekshirish uchun)
app = Flask(__name__)

@app.route('/')
def server_holati():
    return "Bot ishlayapti! ✅", 200

# Bot uchun kerakli ma'lumotlar
API_ID = int(os.getenv("API_ID", 24410919))  # Agar .env faylida bo'lmasa, 24410919 ishlatiladi
API_HASH = os.getenv("API_HASH", "11a3a20ee4f9e851e35412b0a2eedb3a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7761148498:AAGbFdR2gda_1ZPMEtifoW4qv186Cmg6tFI")

# Telegram botini yaratamiz
bot = Client(
    name="mening_botim",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,  # Render.com uchun muhim
    workers=4,       # 4 ta ishchi - optimal son
    plugins=dict(root="plugins")
)

# Bot javoblari lug'ati
JAVOBLAR = {
    "salom": [
        "Salom! Qanday ketyapti? 😊",
        "Assalomu alaykum! 👋",
        "Salom, do'stim!",
        "Yaxshi kun!",
        "Salom! Ishlaringizni qilib yurganingizni ko'rib turibman!",
        "Salom! Yangi kunni qanday kutyapsiz?"
    ],
    "qandaysan": [
        "Zo'r! Siz-chi? 😃",
        "Juda yaxshi! 😊",
        "Ajoyib!",
        "Yaxshi, rahmat!",
        "O'zgarishlar bo'lyapti, sizni qanday kayfiyatda?",
        "Qanday kayfiyatdasiz?"
    ],
    # ... boshqa javoblaringizni shu yerda qoldiring
}

# /start buyrug'i uchun handler
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    try:
        await message.reply_text("Assalomu alaykum! Men Sinfdoshlar 2009 Botiman. Qanday yordam bera olaman! 😊")
    except Exception as xato:
        logger.error(f"Start buyrug'ida xato: {xato}")

# Matnli xabarlar uchun handler
@bot.on_message(filters.text & ~filters.command("start"))
async def javob_ber(client, message):
    try:
        matn = message.text.lower().strip()
        for kalit, javoblar in JAVOBLAR.items():
            if kalit in matn:
                await message.reply_text(random.choice(javoblar))
                return
        
        await message.reply_text("Bu haqida nima deb o'ylaysiz? 🤔")
    except Exception as xato:
        logger.error(f"Xabar qayta ishlashda xato: {xato}")

def flaskni_ishga_tushir():
    """Flask serverini ishga tushiramiz"""
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))

def botni_ishga_tushir():
    """Botni ishga tushiramiz (avto-qayta ishga tushirish bilan)"""
    while True:
        try:
            logger.info("Bot ishga tushmoqda...")
            bot.run()
        except Exception as xato:
            logger.error(f"Bot to'xtadi: {xato}. 10 soniyadan keyin qayta ishga tushirilmoqda...")
            time.sleep(10)

if __name__ == "__main__":
    # Flask ni backgroundda ishga tushiramiz
    flask_thread = Thread(target=flaskni_ishga_tushir, daemon=True)
    flask_thread.start()
    
    # Botni ishga tushiramiz
    botni_ishga_tushir()