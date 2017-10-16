# def my_sum(y, z):
# 	# x = y + z
# 	return y + z

# print(my_sum(2, 3))

# def my_div(x, y): # позиционные аргументы
# 	return x / y

# print(my_div(2, 5))

# def lucky_list(judge, victim, sherif, executioner):
# 	print(sherif + " требует екзекуции \
# и справедливости")
# 	print(judge + " благославляю на казнь!")
# 	print(executioner + " отправил " + victim +
# 	 " на курсы по Паскалю")

# lucky_list(victim = "Сулейманчик", executioner = "Гаджи", 
# 	sherif = "Гоминид", judge = "Бабушка Аня") # аргументы - ключевые слова

# def freud(victim, is_mad = True):
# 	if is_mad == True:
# 		print("Фреид, радостно потирая руки, достает сигару и тушит об " + victim)
# 	elif is_mad == False:
# 		print("Фреид с грустью зажигает сигару от пламени сердца " + victim)
# 	else:
# 		print("Вы и есть Фрёид")

# freud("Эльдар")

# print(10, 15, 123, "Эльдар", sep = " <3 ")
# print(10, 15, 123, "Эльдар", sep = " больше ")

def reptiliod_list(*args, **kwargs):
	print("Остерегайтесь их:", args)
	print("Стрелять без предупреждения по: ", kwargs)

reptiliod_list("Сулейманчек", "Султанмурад", "Гаджи", 
	"Эльдар", "Вера Андреевян", jidomasson = "Саид",
	lemurian = "Эльдар")
