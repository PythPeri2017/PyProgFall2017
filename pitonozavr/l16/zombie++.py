class Human:
	def __init__(self, name, health, damage):
		self.name = name
		self.health = health
		self.damage = damage

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

def choice_weapon(hero):
	i = int(input("Дорогой друг, перед боем выбери чем будешь воевать\n\
		1 - Нож\n\
		2 - Пистолет\n\
		3 - Винтовка\n\
		4 - Выход\n\
		Ваш выбор:"))
	if i == 1:
		print("Вы выбрали нож")
		hero.damage += 15
		ammo = 100000000000
	elif i == 2:
		print("Вы выбрали пистолет")
		hero.damage = 30
		ammo = 8
	elif i == 3:
		print("Вы выбрали винтовку")
		hero.damage = 50
		ammo = 5
	elif i == 4:
		print("Вы решили завершить игру")
		ammo = 0
	return ammo

def game():
	eldar = Heros("Даша следопыт", 150, 20, 3)
	zombo = Zombie("Ватник", 30, 10)
	count_kill = 0
	while True:
		try:
			ammo = choice_weapon(eldar)
			if ammo == 0:
				break
			if eldar.health > 0:
				print("Поехали")	
			eldar.attack(zombo)
			ammo -= 1
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
			input()
			if (eldar.health<=0):
				print("Слава Навальному! Я сделал все что смог")
				print("Я успел переубедить", count_kill, "ватников")
				break	
		except:
			print("Увы, такого оружия нет, попробуй снова!")	

game()