import sqlite3


def createDb():
    con = sqlite3.connect("incidents.db")

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS incidents")
    
    cur.execute('''
    CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
    );
    ''')

    con.commit()
    con.close()