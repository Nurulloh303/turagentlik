# from telegram._utils import markup

from data.loader import bot
from telebot.types import Message
#
# from keyboards.inline import lang_button

from keyboards.dafault import adabiyot,  ozbek_button, jahon_button, ozbek, jahon


@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    text = f"Assalomu alaykum {first_name} xush kelibsiz!!!, \n\n Bolimni tanlang:"
    bot.send_message(chat_id, text,
                     reply_markup=adabiyot())

@bot.message_handler(func=lambda message: message.text == "📚 oʻzbek adabiyoti")
def sho_uzbek(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Kitobni tanlang: ",
                     reply_markup=ozbek_button())


@bot.message_handler(func=lambda message: message.text == "📚 jahon adabiyoti")
def sho_jahon(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Adiblarni tanlang✅:",
                     reply_markup=jahon_button())



@bot.message_handler(func=lambda message: message.text in ozbek)
def send_adib_books(message: Message):
    chat_id = message.chat.id
    text = message.text
    if text  == "📙 Alisher Navoiy":
        with open("kitoblar/ozbek adabiyoti/majnun.pdf", "rb") as f:
            bot.send_document(chat_id, f, caption="Alisher Navoiy - Majnun va Layli")
    elif text == "📙 Ahmad Lutfiy qozonchi":
        with open("kitoblar/ozbek adabiyoti/lutfiy.pdf", "rb") as f:
            bot.send_document(chat_id, f, caption="Ahmad Lutfiy Qozonchi")
    elif text == "📙 Chingiz Aytmatov":
        with open("kitoblar/ozbek adabiyoti/chingiz.pdf", "rb") as f:
            bot.send_document(chat_id, f, caption="Chingiz Aytmatov")



@bot.message_handler(func=lambda message: message.text in jahon)
def send_jahon_adib(message: Message):
    chat_id = message.chat.id
    text = message.text
    if text == "📙 Jek London":
        with open("kitoblar/jahon adabiyoti/jek_london.pdf", "rb") as f:
            bot.send_document(chat_id, f, caption="Jek London")

    elif text == "📙 Vilyam Shekspir":
        with open("kitoblar/jahon adabiyoti/Vilyam.pdf", "rb") as f:
            bot.send_document(chat_id, f, caption="Vilyam Shekspir")

    elif text == "📙 Fedor Dostoevskiy":
        with open("kitoblar/jahon adabiyoti/Fedor.pdf", "rb") as f:
            bot.send_document(chat_id, f, caption="Fedor Dostoevskiy")
