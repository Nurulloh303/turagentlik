
from data.loader import bot, db
import handlers



if __name__ == '__main__':
    db.create_table_users()
    print("Bot ishladi...")
    bot.infinity_polling()