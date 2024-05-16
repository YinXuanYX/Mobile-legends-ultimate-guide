import sqlite3

connection = sqlite3.connect('items.db')

#create a cursor
cursor = connection.cursor()

#create a Table
cursor.execute("create table items (attributes text, passive text, unique_passive text)")


#datatypes 1)NULL (DOESNT EXIST) 2) INTEGER (WHOLE NUM)\
# 3) REAL (DECIMAL) 4) TEXT (TEXT) 5) BLOB (STORE EXACTLY LIKE HOW IT IS LIKE IMG AND MP3)
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]  

cursor.executemany("insert into items values (?, ?, ?)", release_list)


#print database rows
for row in cursor.execute("select * from items"):
    print(row)


# Print specific rows
print("***********************")
cursor.execute("SELECT * FROM items WHERE unique_passive = :c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)





#commit the command
connection.commit()

#close the cnnection
connection.close