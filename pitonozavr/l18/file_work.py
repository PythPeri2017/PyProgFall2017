f = open("NewFile.txt", "w")
f.write("Первая запись")
f.close()
f = open("NewFile.txt", "r")
print("В нашем файле хранится", f.read())
f.close()
f = open("NewFile.txt", "a")
group_list = ['Юнус', 'Гаджи', "Наби", "Тимур"]
i = 1
for name in group_list:
	f.write(str(i) + ": " + name + '\n')
	i += 1
f.close()
f = open("NewFile.txt", "r")
for name in f:
	print(name.rstrip("\n"))
f.close()	