class Cinema:
	def __init__(self,long_time,name,mark):
		self.__long_time = long_time
		self.__name = name
		self.__mark = mark

	def go(self):

		print("зато лучше чем 'Защитники Россий'")

	@property
	def mark(self):
		return "Россия Лезгинам "
	@mark.setter
	def mark(self,value):
		print("фильм и так прикраасен")
	
	@property
	def long_time(self):
		return self.__long_time/3
	@long_time.setter
	def long_time(self,value):
		print(self.__long_time - value)

	@property
	def name(self):
		return "тебе не нужно"
	@name.setter
	def name(self,value):
		print(self.__name)

thor = Cinema(120,"Тор","5/10")
print(thor.long_time)
print(thor.mark)
print(thor.name)
