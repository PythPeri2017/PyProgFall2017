# Алгоритм: 
# 	1) Создаем базовый класс - Человек
# 	2) Создаем два класса - Зомби и Игрок, которые 
# 		будут наследовать класс Человек
# 	3) Созадем метод attack - для моделирования драки
# 	4) Игра на рекорд( количество убитых зомби)
# 	5) Игра кончается со смертью гл.персонажа 

class Human:
	def __init__(self, name, health, damage):
		self.name = name
		self.health = health
		self.damage = damage

	def choice_weapon(self):
		i = int(input("Пожалуйтса, выбирайте оружие:\n\
			1 - Нож\n\
			2 - Пистолет\n\
			3 - Граната"))
		if i == 1:
			print("Пуля дура - штык молодец!")
		elif i == 2:
			print("Пистолет хорош")
		elif i == 3:
			print("Смотри сам не взорвись")

	def attack(self, target):
		print(self.name, "нанес", self.damage, "урона по", target.name)
		target.health -= self.damage
		print("После атаки у", target.name, "осталось", target.health, "здоровья")

class Heros(Human):
	def __init__(self, name, health, damage, medical_box):
		super().__init__(name, health, damage)
		self.medical_box = medical_box

	def heal(self):
		if self.medical_box > 0:
			print("Вы воспользовались аптечкой")
			self.health += 10
			self.medical_box -= 1
		else:
			print("К сожалению аптечек больше нет. Терпи!")

	def whoop(self):
		print("Хэдшот!")

class Zombie(Human):
	def dead_whoop(self):
		print("Хайль ЕР!")

def game():
	eldar = Heros("Даша следопыт", 150, 20, 3)
	zombo = Zombie("Ватник", 30, 10)
	count_kill = 0
	while True:
		try:
			if eldar.health > 0:
				print("Поехали")
				eldar.choice_weapon()
		except:
			print("Вводи число, а не хрень всякую!")
		else:		
			eldar.attack(zombo)
			if zombo.health <= 0:
				zombo.dead_whoop()
				count_kill += 1
				eldar.whoop()
				zombo = Zombie("Ватник", 30, 10)
			else:
				zombo.attack(eldar) 
			print(eldar.name,"хотите воспользоваться аптечкой?")
			i = int(input("1 - да, 2 - нет"))
			if i == 1:
				eldar.heal()
		finally:
			input()
			if (eldar.health<=0):
				print("Слава Навальному! Я сделал все что смог")
				print("Я успел переубедить", count_kill, "ватников")
				break		

game()





