import random

def create_fighter():
	person = {"сила": 100, "выносливость": 1000}
	person["имя"] = input("Введи имя, юнец! ")
	choose = input("1 - прирост к силе, \
		2 - прирост к выносливости ")
	if choose == "1":
		person["сила"] += 40
	else:
		person["выносливость"] += 400
	return person

def health(player):
	print("У игрока", player["имя"], "осталось", 
		player["выносливость"], "выносливости")

def attack(attacker, defender):
	damage = random.randint(attacker["сила"] - 30,
		attacker["сила"] + 30)
	print("Игрок", attacker["имя"], "нанес", 
		damage, "урона")
	defender["выносливость"] -= damage


person1 = create_fighter()
person2 = create_fighter()

while True:
	health(person1)
	health(person2)
	attack(person1, person2)
	attack(person2, person1)
	input()

	if person1["выносливость"] <= 0:
		print(person1["имя"], "проиграл")
		break
	if person2["выносливость"] <= 0:
		print(person2["имя"], "проиграл")
		break
