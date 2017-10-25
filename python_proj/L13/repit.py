class Car:
	def __init__(self, color, firm):
		self.color = color 
		self.firm = firm

	def signal (self):
		print("Бим бим бим")

volga = Car("Красный", "Газ")
volga.signal()
# Car.signal(volga)
print(volga.color)

class Cargo_car(Car):
	def __init__(self, color, firm, carrying):
		super().__init__(color, firm)
		self.carrying = carrying

	def signal(self):
		print("ТА-ДАААМ!")

belaz = Cargo_car("Желтый", "Белаз", 450000)
belaz.signal()

