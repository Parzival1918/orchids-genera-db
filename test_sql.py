import sqlite3

#Create connection to database
conn = sqlite3.connect("db/sqlite/orchids.db")
cursor = conn.cursor()

#Find genera that start with "A"
cursor.execute("SELECT * FROM orchids WHERE name LIKE 'A%'")
rows = cursor.fetchall()

#Print results
for row in rows:
    #Print only the name
    print(row[0])

#Close connection
conn.close()