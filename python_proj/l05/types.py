week = ("Monday", "Tuesday", "Wednesday") # кортеж
print(week[1])
week2 = "Thursday", "Friday"
# week3 = "Saturday",
# print(week3)
# full_week = []
# full_week.append(week)
# print(full_week)
a, b = week2
print(a, b)
x, y, z = "ПН", "ВТ", "СР"
print()

pupils = {"Карл Маркс", "Альберт Эйнштейн", \
"Султанмурад", "Ч. Дарвин", "Карл Маркс"} # множество
print(pupils)
if "Карл Макс" in pupils:
	print("Карл Маркс победил!! Коммунизм по всей планете!")
else:
	print("Забудь о коммунах!")

madteam = {"Карл Маркс", "Альберт Эйнштейн",\
 "Джон Нэш", "Дональд Трамп", "Мальчик-ракета"}
print(pupils & madteam) # пересечение
print(pupils | madteam) # объединение
print(pupils - madteam) # вычитание
print(madteam - pupils)

print("-" * 50)

films = {
	"Люся": "Люся получает супермозг",
	"Безумный Маркс": "Земля превратилась в пустыню - коммунизм победил!",
	"Защитники": "Наш ответ Западу! Медведь, узбек, казах, деваха-невидимка - суперскуад"
}
print(films["Защитники"])
films["Люся"] = "Люся теряет костный мозг"
print(films)
films[7] = "жестокий фильм про семь смертных грехов"
print(films[7])
films["Человек-паук 1" , "Второй человек паук"] = ["Слив", "Шлак", "Чем больше сила, тем больше ответственность!!!", "Дядя Бэн!!"]
print(films["Человек-паук 1" , "Второй человек паук"])

for film in films: # перебор по ключу
	print(film)
	if film =="Люся":
		print("Позор!!")

for description in films.values(): # перебор по значению
	print(description)

for name, desc in films.items(): #перебор по парам - ключу и значению
	print("Фильм " + str(name) + ". Описание: " + str(desc))