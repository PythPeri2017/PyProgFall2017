print("Вы очнулись на помойке. Вокруг, неожиданно, мусор.")
act = input("""Ваши действия: 
1.Покопаться в мусоре.
2.Начать уплетать мусор за обе щеки.
3.Собрать компьютер из окружающих вас отходов
""")
if act == "1":
	print("Вы откопали бомжа. Теперь он следует за вами как питонец")
	act = input("""Ваш питонец проголодался и настроен решительно.
1. Покормить его мусором
2. Сказать 'Перебьешься'
3. Отгрызть ему одну руку и скормить второй руке
""")
	if act == "1":
		print("Случилось неожиданное - он стал человеком года")
	elif act == "2":
		print("Парниша набросился на вас. \
			Годы потребления мусора сделали его довольно сильным. \
			Ваша жизнь закончилась в его желудке.")
	else:
		print("Первая рука срегенировала, а вторая стала еще здоровее и обрела свой разум.")
elif act == "2":
	print("Мусор оказался радиоактивным. Вы обрели суперспособность - вы человек-мусор")
else:
	print("У вас получился Toshiba на Висте - ничего удивительного")