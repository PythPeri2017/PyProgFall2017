class Drinks:
	def __init__(self,name,color,price):
		self.name = name
		self.color = color
		self.price = price
	def smell(self):
		print("Пахнет не очень плохо.")

easy = Drinks("Чай" , "Синий" , 35000)
easy.smell()
#Drinks.smell(easy)
print(easy.name)
class Juice(Drinks):
	def __init__(self,name,color,price,fruit):
		super().__init__(name,color,price)
		self.fruit = fruit

	def smell(self):
		super().smell()
		print("воняет апельсином")

apple = Juice("яблочный","зеленый",99,"яблока")
apple.smell()

