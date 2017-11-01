class Laze:
	def __init__(self, level, long_sleep, age):
		self.__level = level
		self.__long_sleep = long_sleep
		self.age = age

	def sleep(self):
		print(self.long_sleep*"ZZZZzzzzzz")

	@property
	def level(self):
		return self.__level / 2
	@level.setter
	def level(self, value):
		print("Чем меньше - тем лучше")
		print(self.__level + value)
		return self.__level + value

	@property
	def long_sleep(self):
		return 'Сколько хочу, столько и сплю!'
	@long_sleep.setter
	def long_sleep(self, value):
		print('Нельзя меня будить!')


kamil = Laze(80,24*7,1000)
# kamil.sleep()
# print(kamil._Laze__long_sleep)
# kamil.long_sleep = 8
# print(kamil.long_sleep)
print(kamil.level)
kamil.level = 10
print(kamil.age)
# print(kamil.level)


