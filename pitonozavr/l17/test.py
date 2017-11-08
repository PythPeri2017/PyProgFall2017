f = open("data_base.txt", "r")
test = "FD"
for log in f:
	if test == log.rstrip('\n').split(" : ")[1]:
		print("Yes")
		break
else:
	print("No")