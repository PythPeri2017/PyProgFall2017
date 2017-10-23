class Worker:
	def __init__(self, qualif, salary, expa):
		self.qualif = qualif
		self.salary = salary
		self.expa = expa

	def work(self):
		print("Пашу как чорт")

	def swear(self):
		print("*** ****** на ***!!!")

# petrovich = Worker()
# print(petrovich.salary)
# petrovich.swear()

# ivanich = Worker()
# ivanich.swear()
# print(ivanich.salary)

# eldarich = Worker(True, 0, 2000000)
# print(eldarich.salary)

class Miner(Worker):
	def mine(self):
		print("Я намайнил 0.0001 крипторубль")

# aminka = Miner(True, 0.0001, -10)
# aminka.mine()
# aminka.swear()
# print(aminka.expa)

class Proger(Worker):
	def __init__(self, qualif, salary, expa, language, coffee, name):
		super().__init__(qualif, salary, expa)
		self.language = language
		self.coffee = coffee
		self.name = name

	def attack(self, target):
		print(self.name + " ломанул " + target.name)
		target.iq = 20

	def work(self):
		print("Валяться, попивая кофе у себя на районе")

moloch = Proger(True, 500000, 4, "Pascal + Delphi", "Java", "Малик")

class Gastranomer(Worker):
	def __init__(self, salary, heavy_hand, name):
		self.salary = salary
		self.heavy_hand = heavy_hand
		self.name = name
		self.iq = 50000

	def attack(self, target):
		print(self.name + " со всего маху ударил палкой колбасы и нанес " +
			str(self.heavy_hand) + " " + target.name)

sulik = Proger(0, 0, 0, "Scratch", "McCoffee", "Сулейма")
eldarka = Gastranomer(5, 1000, "Эля")


def fight(fighter1, fighter2):
	fighter1.attack(fighter2)
	fighter2.attack(fighter1)

fight(sulik, eldarka)

print(eldarka.iq)