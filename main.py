from pyrogram import Client, filters
import random

# Bot uchun ma'lumotlar
API_ID = 24410919  # my.telegram.org saytidan oling
API_HASH = "11a3a20ee4f9e851e35412b0a2eedb3a"
BOT_TOKEN = "7761148498:AAGbFdR2gda_1ZPMEtifoW4qv186Cmg6tFI"

# Pyrogram Client yaratish
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# So‘z va javoblar ro‘yxati
javoblar = {
    "salom": [
        "Salom! Qanday ketyapti? 😊",
        "Assalomu alaykum! 👋",
        "Salom, do‘stim!",
        "Yaxshi kun!",
        "Salom! Ishlaringizni qilib yurganingizni ko‘rib turibman!",
        "Salom! Yangi kunni qanday kutyapsiz?"
    ],
    "qandaysan": [
        "Zo‘r! Siz-chi? 😃",
        "Juda yaxshi! 😊",
        "Ajoyib!",
        "Yaxshi, rahmat!",
        "O‘zgarishlar bo‘lyapti, sizni qanday kayfiyatda?",
        "Qanday kayfiyatdasiz?"
    ],
    "rahmat": [
        "Arzimaydi! 😊",
        "Har doim yordam berishga tayyorman!",
        "Sizga ham rahmat! 🙏",
        "Rahmat! Barchamiz birga yaxshiroq bo‘lamiz!",
        "Rahmat, do‘stim!"
    ],
    "nima gap": [
        "Hammasi joyida! Sizda-chi? 😊",
        "Yangi yangiliklar bormi?",
        "Hayot davom etmoqda!",
        "Hali yangi narsalar o‘rganib, rivojlanishga tayyorman!"
    ],
    "kim": [
        "Bu savolga aniq javob bera olmayman. 🤷‍♂️",
        "Kimligini aniqlash qiyinroq ekan!",
        "Kim haqida so‘rayapsiz?",
        "Kimgadir o‘xshaysiz, lekin kim ekanini bilmayman.",
        "Kimni nazarda tutyapsiz?"
    ],
    "nima": [
        "Ko‘proq tushuntirib bera olasizmi? 🤓",
        "Aniqroq so‘rashingiz mumkinmi?",
        "Bu haqida batafsilroq bilmoqchiman.",
        "Nima haqida gaplashmoqchisiz?",
        "Buni qanday tushunasiz?"
    ],
    "qayerda": [
        "Aniq ayta olmayman, lekin bilib ko‘raman! 🧐",
        "Shu yerda! 😃",
        "Manzilni aniq bilasizmi?",
        "Qayerda bo‘lishni hohlaysiz?",
        "Qayerga borishni rejalashtirgan edingiz?"
    ],
    "sevgi": [
        "Sevgi juda ajoyib tuyg‘u! ❤️",
        "Sevgi haqida uzoq gapirish mumkin... 😊",
        "Sevgi – hayot mazmuni!",
        "Sevgi har doim eng katta kuchdir! 💖",
        "Sevgi, sadoqat va hurmat – hayotning eng yaxshi tarkibiy qismlari!",
        "Sevgi dunyoni o‘zgartiradi!"
    ],
    "hazil": [
        "Hazillar yaxshi kayfiyat beradi! 😂",
        "Kulgu umrni uzaytiradi deyishadi!",
        "Hazil qilaymi? 😆",
        "Kulib, yaxshi kayfiyatga ega bo‘laylik!",
        "Hazilni sevaman! 😂"
    ],
    "ish": [
        "Ishlaringiz yurishsin! 👍",
        "Omad tilayman! 🚀",
        "Ish bo‘lsa, rivoj bo‘ladi!",
        "Ishlaringizni davom ettirib, o‘z maqsadlaringizga yetasiz!",
        "Ishda muvaffaqiyatlar tilayman!"
    ],
    "yaxshi": [
        "Yaxshi, juda yaxshi! 😊",
        "O'zingizni qanday his qilmoqdasiz?",
        "Yaxshi bo‘lishga harakat qilaman!",
        "Yaxshi, yana qanday yangiliklar?",
        "Yaxshi kayfiyatda qoling!"
    ],
    "qachon": [
        "Qachon nima? ⏳",
        "Qachon so‘rasangiz, men har doim tayyorman!",
        "Qachon biror narsa sodir bo‘ladi? Qiziq!",
        "Vaqt bor, lekin qachonligini bilmayman. 😅",
        "Qachon so‘rasangiz, yordam beraman!"
    ],
    "ishq": [
        "Ishq – bu qalbning eng chuqur tuyg‘usi! 💘",
        "Ishqni anglash juda qiyin, ammo mukammal tuyg‘u! 💖",
        "Ishqni so‘zlar bilan ifodalab bo‘lmaydi, uni his qilmoq kerak!"
    ],
    "do‘stim": [
        "Do‘stim, seni ko‘rganimdan xursandman! 😄",
        "Do‘stim, yordam kerakmi?",
        "Do‘stim, qanday kayfiyatdasiz?",
        "Siz bilan do‘st bo‘lish juda yaxshi!"
    ],
    "xush": [
        "Xush, qalay?",
        "Xush, baxtiyor bo‘lishingizni tilayman!",
        "Xush kelibsiz! Yaxshi kayfiyatda qoling!",
        "Xush kelibsiz, baxtli bo‘ling!"
    ],
    "hammamiz": [
        "Hammamiz birga kuchlimiz! 💪",
        "Birgalikda biz hammasiga erishamiz! 🌟",
        "Hammamizni bir-birimiz qo‘llab-quvvatlashimiz kerak!"
    ],
    "yaxshi kayfiyat": [
        "Yaxshi kayfiyatda qoling! 😊",
        "Har doim yaxshi kayfiyatda bo‘lishga harakat qilaman!",
        "Yaxshi kayfiyat – eng yaxshi motivatsiya!"
    ],
    "kun": [
        "Kun qanday o'tmoqda? 🌞",
        "Bugun qanday kun bo‘ldi? 🌻",
        "Kun hali yakunlanmagan, qanday his-tuyg‘ulardasiz?"
    ],
    "yordam": [
        "Yordam kerakmi? 😊",
        "Har doim yordam berishga tayyorman!",
        "Yordam so‘rayapsizmi? Biror narsa bor!"
    ],
    "yashash": [
        "Yashash – eng katta imkoniyat! 🌱",
        "Hayotda yashashdan ko‘ra yaxshi narsa yo‘q!",
        "Yashash bizga berilgan eng katta sovg‘a!"
    ],
    "dostlik": [
        "Dostlik – dunyodagi eng qadrli tuyg‘u! 👫",
        "Dostlikning kuchi hech qachon kamaymaydi!",
        "Dostlarimiz bizning kuchimizdir!"
    ]
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

    message.reply_text("Bu haqida nima deb o‘ylaysiz? 🤔")

# Botni ishga tushirish
bot.run()
