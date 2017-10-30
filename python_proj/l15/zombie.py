# Создать класс Human и подклассы player и zombie. 
# Игрок и зомби дерутся. Умирает зомби - появляется зомби.
# Умирает игрок - игра окончена.

class Human:
	def __init__(self, health, damage):
		self.health = health
		self.damage = damage

	def attack(self, target):
		target.health -= self.damage
		print("Нанес урон", self.damage)

class Player(Human):
	def __init__(self, health, damage, count_kit):
		super().__init__(health,damage)
		self.count_kit = count_kit

	def heal(self):
		if self.count_kit > 0:
			self.count_kit -= 1
			self.health += 10
			print("Вы воспользовались аптечкой. Ваше здоровье:", self.health)
		else:
			print("Cорян, аптечек больше нет, терпи!")

class Zombie(Human):
	def death(self):
		print("Уааааа")

def game():
	count_kill = 0
	sidor = Player(125, 20, 3)
	zombie = Zombie(30, 5)
	while True:
		sidor.attack(zombie)
		input()
		zombie.attack(sidor)
		input()
		if zombie.health <= 0:
			zombie.death()
			zombie = Zombie(30, 5)
			count_kill += 1

		print("Ваш уровень здоровья", sidor.health,
			"Вы хотите воспользоваться аптечкой?")
		i = int(input("1 - Да" + " 2 - Нет"))
		if i == 1:
			sidor.heal()

		if sidor.health <= 0:
			print("Сидорович умудрился замочить", count_kill,
				"и пал смертью храбрых, теперь сталкерам некому нести хабар")
			break

game()
