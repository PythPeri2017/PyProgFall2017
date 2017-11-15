import sqlite3

db = sqlite3.connect("GunsShop.db")
myCursor = db.cursor()

myCursor.execute("""UPDATE GunsShop
	SET Name = 'AK-74'
	WHERE Name = 'апщвазпщ'
	""")

myCursor.execute("DELETE FROM GunsShop WHERE Id = 1")

myCursor.execute("SELECT Name, Price FROM GunsShop ORDER BY Price DESC")
a = myCursor.fetchall()
#print(a)
for i in a:
	print(i)
myCursor.close()
db.close()