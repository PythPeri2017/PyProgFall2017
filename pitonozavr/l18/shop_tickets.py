class Users:
	def __init__(self, login, password):
		self.login = login
		self.password = password

	def register(self):
		f = open("List_of_users.txt", "r+")
		for log in f:
			if self.login == log.split(" : ")[0]:
				print("Пользователь с таким именем уже есть")
				break
		else:
			f.write(self.login + " : " + self.password + "\n")
			print("Регистрация прошла успешно! Шаааа!!!")
		f.close()

	def autorize(self):
		bool_aut = False
		f = open("List_of_users.txt", "r")
		for log in f:
			if self.login == log.split(" : ")[0] and self.password == log.rstrip("\n").split(" : ")[1]:
				print("Авторизация прошла успешно")
				bool_aut = True
				break
		else:
			print("Не удается авторизоваться")
			choice = input("1 - Ввести данные заново\n2 - Зарегистрироваться")
			if choice == "1":
				self.login = input("Введите логин")
				self.password = input("Введите пароль")		
				self.autorize()
			elif choice == "2":
				self.register()
			else:
				print("Error 404: Ты черт!")
		f.close()
		return bool_aut

def show_tickets():
	f = open("Shop_list.txt", "r")
	print("Список билетов:")
	for tick in f:
		print(tick.rstrip("\n"))
	f.close()

def buy_tickets(user):
	f = open("Shop_list.txt", "r")
	basket_f = open("Basket.txt", "a")
	basket_f.write("Список покупок пользователя " + user.login + "." + '\n')
	name = input("Введи название билета:")
	while True:
		show_tickets()
		i = input("Для выхода из меню покупок введите 0")
		if i == "0":
			break
		for bask in f:
			print(bask.split(" : ")[0])
			if name == bask.split(" : ")[0]:
				print("Билет успешно найден и добавлен в корзину")
				basket_f.write(bask)
				break
		else:
			print("Билет не найден")




i = input("1 - Войти\n2 - Зарегистрироваться")
user = Users(input("Введите логин:"), input("Введите пароль:"))
bool_aut = user.autorize()
if bool_aut == True:
	buy_tickets(user)
else:
	print("Вы не авторизованы")