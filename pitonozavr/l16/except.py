class MyError(Exception):
	pass

class AnimeDag:
	brain = None
	count_hromo = 47

class Culc:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def summ(self):
		return self.x + self.y

	def subt(self):
		return self.x - self.y

	def multi(self):
		return self.x * self.y

	def division(self):
		return self.x / self.y
try:
	dino = AnimeDag()
	my_list = [1, 2, 0]
	x = int(input("Введите первое число:"))
	y = int(input("Введите второе число:"))
	if x == 13 or y == 13:
		raise MyError(dino)
	number = Culc(x, y)
	print(number.division())
except ZeroDivisionError as word:
	print("Произошла ошибка:", word)
except (IndexError, ValueError) as word:
	print("Произошла ошибка:", word)
except MyError as word:
	word.brain = 47
	print("- У меня",word.brain, "хромосом","\n- Боже упаси и сохрани!")
