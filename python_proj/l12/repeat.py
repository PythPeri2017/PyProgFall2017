# class Human():
# 	bipedalism = True
# 	intellect = 999
# 	def speech(self):
# 		print("Я человек")
# firstman = Human()
# print("Уровень интелекта -",firstman.intellect)
# firstman.speech()

# secondman = Human()
# print(secondman.intellect)
# firstman.speech()

class Cat():
	def __init__(self, jump, tail_length, mind):
		self.jump = jump
		self.tail_length = tail_length
		self.mind = mind

	def Meow(self):
		print("Мяуууу!")

tom = Cat(100, 1, 500)
# print(tom.jump)

barseek = Cat(20, 50, int(input("Введите разум")))
print(barseek.mind)

if tom.mind > barseek.mind:
	print("Том мудр!")
else:
	print("Том мудр, но Барсик - элита!")