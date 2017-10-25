# class Secret_info:
# 	def __init__(self, data, parols):
# 		self.__data = data

# my_doc = Secret_info("2x2=4")
# # print(my_doc.__data)
# print(my_doc._Secret_info__data)

class Secret_info:
	def __init__(self, info):
		self.secret_parols = info

	def get_secret_parols(self):
		print("Срабатывает геттер")
		return self.secret_parols

	def set_secret_parols(self, new_information):
		print("Срабатывает геттер!!")
		self.secret_parols = new_information + "!!!!"

	parols = property(get_secret_parols, set_secret_parols)

logins = Secret_info("1234")
print(logins.parols)
logins.parols = "10"
print(logins.parols)