from telebot import TeleBot
from config import TOKEN
from database.database import Database

bot = TeleBot(TOKEN)
db = Database()