class Animal:
	def __init__(self, hands, areal, feed):
		self.hands = hands
		self.areal = areal
		self.feed = feed

	def scream(self, name):
		print("ААААА! Где мой " + name + "???")
		print("Я хочу есть " + self.feed)

	def attack(self):
		print("Набросился на соперника всеми " + 
			str(self.hands) + "-мя лапами" )

# revun = Animal(4, "Россия Матушка", "нытье")
# print("Ревун обитает в " + revun.areal)
# revun.scream("Лукман")

class Fish(Animal):
	def swim(self, speed):
		print("Вжух-вжух-вжух " * speed)

# arkadi = Fish(0, "Ак-гёль", "мусор")
# arkadi.scream("ДИИМООООН!")
# arkadi.swim(5)

class Birds(Animal):
	def __init__(self, wings, areal, feed, highs):
		self.wings = wings
		self.areal = areal
		self.feed = feed
		self.highs = highs

	def scream(self):
		print("Супер-КААР!")

	def attack(self):
		print("Начал колотить своими " + 
			str(self.wings) + "-мя крыльями")

# kar_karich = Birds(3, "Чернобыль", "Сталкеры", -10)
# kar_karich.scream()

class EvilBirds(Birds):
	def __init__(self, wings, areal, feed, highs, fangs):
		super().__init__(wings, areal, feed, highs)
		self.fangs = fangs

	def scream(self):
		super().scream()
		print("Я разовру вклочья тебя!!! ыыы")

ruslan = Fish(0, "Средиземье", "букашки")
red = EvilBirds(2, "Повсюду", "Мясо!", 100000, 1)
# print(red.fangs)
# red.scream()
red.attack()
ruslan.attack()