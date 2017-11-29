import telebot

TOKEN = "407705344:AAHPXFofcPZlBF2xCFHCXRAbu2vs99_f4CU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def (message):
	bot.send_message(message.chat.id, "")


if __name__ == "__main__":
	bot.polling()