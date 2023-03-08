import sqlite3

#createDb function to create a new Database
def createDb():
    #creating "incidents.db"
    con = sqlite3.connect("incidents.db")

    #creating cursor to keep track of the index
    cur = con.cursor()

    #Dropping the table if it already exists
    cur.execute("DROP TABLE IF EXISTS incidents")
    
    #Creating the New table
    cur.execute('''
    CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
    );
    ''')

    #Commit the changes and close the connection
    con.commit()
    con.close()