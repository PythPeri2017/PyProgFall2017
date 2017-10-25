class Sheros:
	def __init__(self, name, superpower, archenemy):
		self.name = name
		self.superpower = superpower
		self.archenemy = archenemy

	def superpunch(self):
		print(self.name + " нанес страшнейший " +
			self.superpower + " по " + self.archenemy +
			 ", и взрывная волна разошлась по миру!")

class Watermelon:
	def __init__(self, name, weight, diametr):
		self.name = name
		self.weight = weight
		self.diametr = diametr

	def superpunch(self):
		print(self.name + " накатился всеми своими " + 
			str(self.weight) + " килограммами так, что весь мир взвыл!")	


def strike(hero):
	hero.superpunch()



tor = Sheros("Тор-браузер", 
	"удар молотом блока Роскомнадзора", "ФСБ")
aquaman = Sheros("Аква-мем", "смехотворный удар, призвал Ктулху,\
пса Дратути, вытащил рисунок суперспособности", "Дружко")

arboozman = Watermelon("Петрович", 32000, 1)


strike(tor)
strike(aquaman)
strike(arboozman)
