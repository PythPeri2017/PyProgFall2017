import telebot

TOKEN = "484471277:AAH6nE-6Su4ERRjGA3Jh2jxNYon6OuwmCAc"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["peripil"])
def answer(message):
	bot.send_message(message.chat.id, "Скотина! Где пил, там и ночуй!")

@bot.message_handler(regexp="Сусло")
def suslospam(message):
	i = 1
	while True:
		bot.send_message(message.chat.id, "Суслик намбер 0 " * i)
		i += 1

@bot.message_handler(func=lambda message:True)
def my_messendge(message):
	if message.text == "Мохен":
		bot.send_message(message.chat.id, "Пошел отсюда, гаденыш")
	elif message.text == "Тохен":
		bot.reply_to(message, "Добро пожаловать!")



if __name__ == "__main__":
	bot.polling()