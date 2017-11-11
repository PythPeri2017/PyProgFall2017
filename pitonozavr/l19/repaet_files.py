f = open("Cities.txt","w")
cities_list = ["Makhachkala","Grozniy","Magac","Saint-Peterburg"]
for city in cities_list:
	f.write(city + "\n")
f.close()