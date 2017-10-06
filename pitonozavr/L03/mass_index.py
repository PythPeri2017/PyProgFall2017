mass = int(input("Введите свою вес: "))

if mass <= 25:
	print("Ты при смерти")
elif mass > 25 and mass < 40:
	print("Ты весишь как кошка")
elif 40 <= mass < 60:
	print("Ты весишь как жирная кошка")
elif mass == 150 or mass > 1500:
	print("Ты сверхчеловек")
elif mass > 100 and mass != 666:
	print("ты человек-паук и горишь в аду")
# elif True:
# 	print("Ты лох")
else:
	print("Ты Малик")

# ==, !=, >, <, >=, <=