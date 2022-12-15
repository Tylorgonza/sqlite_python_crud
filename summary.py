import sqlite3
import os.path
import csv

print('SQLite version:')
print(sqlite3.version)

print('Loading the Database')
con = sqlite3.connect('CSCI4333.db')
cur = con.cursor()
print('Success!')

#################################
print("Summary Starts Here:")
#Return total number of musicians and a list of musicians
#group musician by ssn and count

#number 1
musicians = "SELECT Count(DISTINCT ssn) FROM musician M"
res = cur.execute(musicians)
for row in res : num = row
print("1: Number of Musicians: " + str(num[0]))
print("1: List of musicians:")
list_musicians = "SELECT * FROM musician M"
res = cur.execute(list_musicians)
labels = list(map(lambda x: x[0], res.description))
print(labels)
for row in res : print(row)
print('-----------------')

# number 2
albums = "SELECT Count(DISTINCT album_id) FROM album A"
res = cur.execute(albums)
for row in res : num = row
print("2: Number of Albums at Notown: " +str(num[0]))
list_albums = "SELECT * From album A"
res = cur.execute(list_albums)
print("2: List of albums")
labels = list(map(lambda x: x[0], res.description))
print(labels)
for row in res : print(row)
print('-----------------')

#number 3
instruments = "SELECT Count(DISTINCT instrument_id) FROM instrument I"
res = cur.execute(instruments)
for row in res: num = row
print("3: Number of Instruments at Notown: " + str(num[0]))
list_instruments = "SELECT * From instrument I"
res = cur.execute(list_instruments)
print("3: List of instruments")
labels = list(map(lambda x: x[0], res.description))
print(labels)
for row in res : print(row)
print('-----------------')

#number 4
#from musician-album
#need to group by
print("4: Name of Musicians and # of albums by them:")
#statement = "SELECT M.name FROM musician M WHERE M.ssn in (SELECT MA.ssn FROM musicianToalbum MA GROUP BY ssn)"
statement = "SELECT name, Count(DISTINCT album_id) FROM musician NATURAL JOIN musicianToalbum GROUP BY ssn"
#SELECT ssn, Count(DISTINCT album_id) FROM musicianToalbum MA GROUP BY ssn
res = cur.execute(statement)
labels = list(map(lambda x: x[0], res.description))
print(labels)
for row in res: print(row)

con.close()