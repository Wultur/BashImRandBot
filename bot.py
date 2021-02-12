import telebot
import parser
import markups as m


#major variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','go'])
def start_handler(message):
    bot.send_message(message.chat.id, parser.getRandomQuote(), reply_markup=m.start_markup)


bot.polling(none_stop=True)
