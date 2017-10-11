# group = input("Введите состав подразделения, солдат: ")
# print(group)
# group_list = group.split(", ") #split() - разбивал строку
# print(group_list)

# final_group = " <3 ".join(group_list) #join() соединяет в строку
# print(final_group)

# numbers = [3, 11, 5, 30]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# numbers.sort()
# print(numbers)

# guess = int(input("Отгадай число, мальчонка: "))
# print(guess in numbers)

# if guess in numbers:
# 	print("А ю лаки мэн?!")
# else:
# 	print("Пур бастард!")
# print(range(0, 19))
# print(guess in range(0, 19))

# actress = {"Скарлет Йоханнсеннн", "Галя Гадот", "Маргарита"}
# for person in actress:
# 	if person == "Галя Гадот":
# 		print("не так себе " + person)
# 	else:
# 		print("так себе " + person)

# for number in range(0, 100, 3):
# 	print(number)

# phrases = {
# "Ленин": "Учиться и т.д.",
# "Стетхем": "Ин вино веритас",
# "Дядя Бен": "Чем больше, тем больше",
# "Фортран бой": "Нормально делай - нормально будет"
# }

# for phr in phrases.items():
# 	print(phr)

dishes = ["Цезарь", "Тирамису", "Овсянка"]
prices = [100, 50, 1000]

for dish, price in zip(dishes, prices):
	print(dish, " по цене ", price)