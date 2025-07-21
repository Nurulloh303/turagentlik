from data.loader import bot
from telebot.types import Message

@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    text = (f"🇺🇿Assalomu alaykum FN30 tur agentligiga xush kelibsiz!!!\n"
            f"Iltimos tilni tanglang!!!\n\n"
            f"🇬🇧Hello, welcome to FN30 tour agency!!!\nPlease select the language!!!\n\n"
            f"🇷🇺Здравствуйте, добро пожаловать в туристическое агентство FN30!!!\nПожалуйста, выберите язык!!!")
    bot.send_message(chat_id, text)
