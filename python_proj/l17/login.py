class Users():
	def __init__(self, login, password):
		self.login = login
		self.password = password
	def register(self, users_list):
		if self.login in users_list:
			print("Такой пользователь уже существует")
		else:
			users_list[self.login] = self.password
			print("Вы успешно зарегестрировались")

	def aythorize(self, users_list):
		if self.login in users_list:
			print('Успешная авторизация')
		else:
			print('Такой пользователь не существует')
			choice = input('1)Попробовать ещё раз 2)Создать новый аккаунт')
			if choice == '1':
				aythorize(users_list)
			elif choice == '2':
				register(users_list)

def work(users_list):
	#try:
		exit = 0
		choic = input('1)Войти 2)Регистрация 3)Выход')
		if choic == '1':
			user = Users(input('Введите логин:'), input('Введите пароль:'))
			user.aythorize(users_list)
		elif choic == '2':
			user = Users(input('Введите логин:'), input('Введите пароль:'))
			user.register(users_list)
		elif choic == "3":
			f = open("Users.txt" , "a")
			for i in users_list.keys():
				f.write(i+"-"+users_list[i])
			exit = 1
			f.close()
		else:
			print("Ты поступаешь плохо")
	#except:
	#	print("Произошла ошибка")
		return exit
users_list = {}
while True:
	i = work(users_list)
	print(users_list)
	if i == 1:
		break
