import telebot

TOKEN = "407705344:AAHPXFofcPZlBF2xCFHCXRAbu2vs99_f4CU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(regexp="Воланд")
def checker(message):
	bot.send_message(message.chat.id, "STFU")


our_kb = telebot.types.ReplyKeyboardMarkup()
our_kb.row("+", "-")
our_kb.row("*", "/")

@bot.message_handler(commands=["start"])
def start_kb(message):
	bot.send_message(message.chat.id, "Вводите оператор, молодой человек", reply_markup=our_kb)

if __name__ == "__main__":
	bot.polling()