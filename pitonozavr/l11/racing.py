# Описываем участников - скорость, нитро, бак, расход топлива, пройденный путь,
# имя.
# На выбор: обычная скорость, нитро - расход топлива 3x - каждый ход
# Побеждает тот, кто приехал первый, либо тот, у кого позже закончилось
# топливо.

def eezzzee(car):
	car["distance"] += car["speed"]
	car["fuel"] -= car["expen"]

def neeetrooo(car):
	car["distance"] += car["nitro"]
	car["fuel"] -= car["expen"] * 3

def stats(car):
	print("\nТекущее состояние:",
		"Топливо: " + str(car["fuel"]),
		"Расстояние: " + str(car["distance"]) + "/" + str(track),
		sep = "\n"
		)

def step(car):
	choose = input("Твой ход, " + car["name"] + 
		". Что будем делать?\n" +
		"1 - Просто едем\n" +
		"2 - топиим!!\n"
		)

	if choose == "1":
		eezzzee(car)
	elif choose == "2":
		neeetrooo(car)
	else:
		print("Ты ошибся!")

	stats(car)
	input()


track = 50

car1 = {
	"name": "Бэтмобиль",
	"speed": 6,
	"fuel": 35,
	"expen": 3,
	"nitro": 11,
	"distance": 0
}

car2 = {
	"name": "Черная молния",
	"speed": 8,
	"fuel": 30,
	"expen": 4,
	"nitro": 13,
	"distance": 0
}

while True:
	step(car1)
	step(car2)