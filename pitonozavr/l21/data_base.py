import sqlite3

db = sqlite3.connect("GunsShop.db")
db_cursor = db.cursor()

db_cursor.execute("""CREATE TABLE IF NOT EXISTS GunsShop(
	ID INT PRIMARY KEY,
	Name VARCHAR(16),
	Skin VARCHAR(32),
	MaxAmmo INT,
	Price REAL
	)
""")
i = 2
while True:
	queri = "INSERT INTO GunsShop VALUES (?, ?, ?, ?, ?)"
	date = i, input("Введите название оружия: "), input("Введите название скина: "), int(input("Введите кол-во патрон: ")), int(input("Введите цену оружия: "))
	i += 1
	db_cursor.execute(queri, date)
	if input("Для выхода введите 0 ") == "0":
		break
db.commit()
db_cursor.close()
db.close()