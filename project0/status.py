import sqlite3

#Status will return count of nature repeated in all the database
def status(db):
    con = sqlite3.connect(db)
    cur = con.cursor()

#Grouping it by nature
    cur.execute("SELECT nature, COUNT(*) FROM incidents GROUP BY nature")
    rows = cur.fetchall()

#Printing the count and nature
    for row in rows:
        print(row[0]+"|"+str(row[1]))

    con.commit()
    con.close()