f = open("grait.txt", "r")
my_list = f.read().split(" ")
n = 1
for i in my_list:
	print(n, i)
	n += 1