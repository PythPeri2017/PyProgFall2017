import random
def my_class():
	r = random.randint(1,4)
	if r == 1 or r == 2:
		print("Доброе утро!")
	elif r == 3 or r == 4:
		print("НЕ доброе утро!")
my_class()