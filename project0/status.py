import sqlite3

def status(db):
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute("SELECT nature, COUNT(*) FROM incidents GROUP BY nature")
    rows = cur.fetchall()

    for row in rows:
        print(row[0]+"|"+str(row[1]))

    con.commit()
    con.close()