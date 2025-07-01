import sqlite3 as sq

with sq.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("""SELECT * FROM boards""")
    print(cur.fetchall())