import sqlite3


con = sqlite3.connect('Equals.db')
cur = con.cursor()
result = cur.execute("""SELECT id FROM Equal WHERE with_y LIKE 'y = %'""").fetchall()
con.close()
for _ in result:
    print(_[0])