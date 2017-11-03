class MyError(Exception):
	pass

class Bomba:
	chika = True
	def uuu(self):
		print("uuuuuu")

try:
	margo_robbie = Bomba()
	print(margo_robbie.chika)
	i = 10
	raise MyError(margo_robbie)
except MyError as j:
	j.chika = False
	print(j.chika)

