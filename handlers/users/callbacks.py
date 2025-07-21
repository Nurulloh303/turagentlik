from data.loader import bot

from telebot.types import CallbackQuery

@bot.callback_query_handler(func=lambda call: call.data in ["uz", "ру" "en"])
def reaction_to_lang(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.message.from_user.id
    