from telebot.types import KeyboardButton, ReplyKeyboardMarkup

def adabiyot():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("📚 oʻzbek adabiyoti")
    btn2 = KeyboardButton("📚 jahon adabiyoti")
    markup.add(btn1, btn2)
    return markup

ozbek = ["📙 Alisher Navoiy",
         "📙 Ahmad Lutfiy qozonchi",
         "📙 Chingiz Aytmatov"]

jahon = ["📙 Jek London",
         "📙 Vilyam Shekspir",
         "📙 Fedor Dostoevskiy"]

def ozbek_button():
    markup= ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for uzb in ozbek:
        but = KeyboardButton(uzb)
        markup.add(but)

    back = KeyboardButton('ortga')
    markup.add(back)
    return markup

def jahon_button():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for jhn in jahon:
        but = KeyboardButton(jhn)
        markup.add(but)
    back = KeyboardButton('ortga')
    markup.add(back)
    return markup