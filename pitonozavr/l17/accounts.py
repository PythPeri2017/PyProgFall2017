class Users:
	def __init__(self , login , password):
		self.login = login
		self.password = password

	def register(self , list_of_users):
		if self.login in list_of_users:
			print("Такой логин уже используется")
		else:
			list_of_users[self.login] = self.password
			print("Вы успешно зарегистрировались!")

	def authen(self , list_of_users):
		current_list = (self.login , self.password)
		if current_list in list_of_users.items():
			print("Вы успешно авторизовались !")
		else:
			print("Аккаунт не найден.")
			x = input("1 - Создать аккаунт \n \
			2 - Попробуй снова ")
			if x == "1" :
				self.register(list_of_users)
			elif x == "2" :
				self.authen(list_of_users)
			else:
				print("Плохой ты малыш!")

def main_worker(list_of_users):
	break_cycle=False
	choice = input("Добро пожаловать на наш сайт\n \
	Для того чтобы войти - 1 \n \
	 2 - зарегистрироваться \n \
	 3- выйти   ")
	if choice == "1":
		user = Users(input("Логин: "),input("Пароль: "))
		user.authen(list_of_users)
	elif choice == "2":
		user = Users(input("Логин: "),input("Пароль: "))
		user.register(list_of_users)
		file = open("data_base.txt", "a")
		file.write(user.login + " : " + user.password + "\n")
		file.close()
	elif choice=="3":
		break_cycle=True
	else: 
		("Животное ")		
	return break_cycle

eldar = {}
while True:
	break_cycle=main_worker(eldar)
	print(eldar)
	if break_cycle==True:
		print("Вы успешно вышли! ")
		break