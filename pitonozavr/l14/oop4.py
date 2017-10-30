class Planet:
	def __init__(self, name, mass, satelite):
		self.name = name
		self.secret_mass = mass
		self.satelite = satelite

	def get_mass(self): # Это getter - отдает 
 		return self.secret_mass

	def set_mass(self, value): # Это setter - меняет
		self.secret_mass = value

	our_mass = property(get_mass,set_mass)

	


def rotate(my_planet):
	if my_planet.satelite == True:
		print("У меня есть спутник")
	else:
		print("У меня нет спутника")

earth = Planet("Земля", "5*10^24", True)
#rotate(earth)
x = earth.our_mass
print(x)
earth.our_mass = "asdf"