import sqlite3

conn = sqlite3.connect("List_of_worker.db")
cur = conn.cursor()

cur.execute("SELECT surname, name, post, record FROM List_of_worker WHERE name == 'Gadji' AND surname == 'Aigumov'")

info = cur.fetchall()
print(info)

cur.close()
conn.close()