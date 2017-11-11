f = open("Cities.txt","r")
b=0
for i in f:
	b+=1

	print(str(b) +'.'+ i.rstrip('\n') )