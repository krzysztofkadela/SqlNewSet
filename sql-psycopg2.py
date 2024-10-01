import psycopg2

# connect to "chinok" database
connection = psycopg2.connect(database="chinok")

#build a cursor object of the database

cursor = connection.cursor()

#Query 1 - select all records from the "Artist" table

#cursor.execute('SELECT*FROM "Artist"')
#cursor.execute('SELECT "Name" FROM "Artist"')
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# fetch the results(multiple)

results = cursor.fetchall()

#fetch the results (single)
#results = cursor.fetchone()


#close the connection
connection.close()

#print results

for result in results:
    print(result)