import telebot

TOKEN = "484471277:AAH6nE-6Su4ERRjGA3Jh2jxNYon6OuwmCAc"

bot = telebot.TeleBot(TOKEN)

keyb = telebot.types.ReplyKeyboardMarkup()
keyb.row("Лига справедливости", "Азербайджан сегодня")
keyb.row("Система 05", "Последний боготур")

@bot.message_handler(commands=["my_kb"])
def create_kb(message):
	bot.send_message(message.chat.id, "Отправь название фильма", reply_markup=keyb)


@bot.message_handler(commands=["get_sp"])
def spoilering(message):
	line_-kb = telebot.types.InlineKeyboardMarkup()
	url_btn = telebot.types.InlineKeyboardButton(text="Жми и перейдешь на сайт!", url="http://www.google.com")
	line_kb.add(url_btn)

	my_button = telebot.types.InlineKeyboardButton(text="Пополнение счета", callback_data="1000")
	line_kb.add(my_button)

	bot.send_message(message.chat.id, "Нажимай уже!", reply_markup=line_kb)

@bot.callback_query_handler(func=lambda call:True)
def do_callback(call):
	if call.data == "1000":
		bot.send_message(call.message.chat.id, "вы получили " + call.data)


if __name__ == "__main__":
	bot.polling()