token =""
import telebot



bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    word = 'sveta'
    string = message.text.lower()
    if word in string:
        bot.send_message(message.chat.id, 'Ба! Знакомые все лица!')
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
