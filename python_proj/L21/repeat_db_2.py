import sqlite3

conn = sqlite3.connect("List_of_worker.db")
cur = conn.cursor()

cur.execute("SELECT surname, post, record FROM List_of_worker ORDER BY record DESC")

info = cur.fetchall()
print(info)

cur.close()
conn.close()