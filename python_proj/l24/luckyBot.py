import telebot

TOKEN = "407705344:AAHPXFofcPZlBF2xCFHCXRAbu2vs99_f4CU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["hello"])
def answer(message):
	bot.send_message(message.chat.id, "Ваалейкум привет")

@bot.message_handler(func=lambda message:True)
def say_smth(message):
	if message.text == "Здрасте":
		bot.send_message(message.chat.id, "Пошел вон!")
	elif message.text == "Здровеньки булы":
		bot.reply_to(message, "Оооо, братан!")


if __name__ == "__main__":
	bot.polling()