import sqlite3

descriptor = sqlite3.connect("List_of_worker.db")
curok = descriptor.cursor()
curok.execute("DROP TABLE List_of_worker")

curok.execute("""CREATE TABLE IF NOT EXISTS List_of_worker (
	id INT PRIMARY KEY,
	surname VARCHAR(30),
	name VARCHAR(25),
	post VARCHAR(20),
	record REAL)
	""")

curok.execute("INSERT INTO List_of_worker VALUES(1,'Ivanov','Ivan','Director',5)")
curok.execute("INSERT INTO List_of_worker VALUES(2,'Petrov','Petr','Accountant',3)")
curok.execute("INSERT INTO List_of_worker VALUES(3,'Zulpicarov','Ruslan','HR manager',4)")
curok.execute("INSERT INTO List_of_worker VALUES(4,'Magomedov','Shamil','Senior Python Developer',7)")
curok.execute("INSERT INTO List_of_worker VALUES(5,'Ataev','Vladimir','Senior Python Developer',6)")
curok.execute("INSERT INTO List_of_worker VALUES(6,'Aigumov','Gadji','Senior Python Developer',5)")



descriptor.commit()
curok.close()
descriptor.close()
