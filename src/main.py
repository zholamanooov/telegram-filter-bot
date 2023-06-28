import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

triggers=['Smoke','Меня зовут Smoke']

@bot.message_handler(func=lambda message: message.text == message.text in triggers)
def handle_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    member = bot.get_chat_member(chat_id, user_id)

    if member.status == "administrator" or member.status == "creator":
        bot.send_message(chat_id, 'sigma')
    else:
        bot.delete_message(chat_id, message.message_id)



bot.infinity_polling()
