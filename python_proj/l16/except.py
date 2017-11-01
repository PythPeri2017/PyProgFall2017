class MyError(Exception):
	pass
class Calculat:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def summ(self):
		return self.x + self.y

	def diff(self):
		return self.x - self.y

	def multiplicat(self):
		return self.x*self.y

	def division(self):
		return self.x / self.y
try:
	my_list = [1,2,3]
	x = int(input("Введи первое число: "))
	y = int(input("Введи второе число: "))
	if x == 13 or y == 13:
		raise MyError("SMS")
	number = Calculat(x, y)
	print(number.division())
	print("Я могу прекрасно работать дальше")
except ZeroDivisionError as word:
	print("Возникла следующая ошибка", word)
except IndexError as word:
	print("Возникла следующая ошибка", word)
except (TypeError, ValueError) as word:
	print("Возникла следующая ошибка", word)
except MyError as word:
	print("Возникла наша ошибка", word)
except:
	print("Возникла неизвестная ошибка")

