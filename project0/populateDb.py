import sqlite3

def populateDb(db, data):
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.executemany('''
    INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)
    VALUES (?, ?, ?, ?, ?);
    ''', data)


    con.commit()
    con.close()
