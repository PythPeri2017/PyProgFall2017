f = open("data_base.txt", "r")
for i in f:
	print(i.split(" : ")[1])
	print("FD" == i.split(" : ")[1])