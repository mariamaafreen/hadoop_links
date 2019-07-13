import sqlite3

conn = sqlite3.connect('links.db')

c = conn.cursor()


c.execute("SELECT * from hadoop")

print(c.fetchall())


conn.commit()

conn.close()






