import sqlite3
import os.path
import csv

print('SQLite version:')
print(sqlite3.version)

con = sqlite3.connect('CSCI4333.db')
cur = con.cursor()



#################################
#Create Musician
#################################

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='musician' ''')

if cur.fetchone()[0]==0:
    print("CREATING TABLE")
    statement = '''
            CREATE TABLE musician (
                          num text, 
                          street text, 
                          str_type text,
                          name text,
                          ssn text,
                          PRIMARY KEY(ssn)
                          );
            '''
    #inserting records from csv
    cur.execute(statement)
    file = open('musician.csv')
    contents = csv.reader(file)
    contents = [x for x in contents]
    insert_records = "INSERT INTO musician (num, street, str_type, name, ssn) VALUES(?,?,?,?,?)"
    cur.executemany(insert_records,contents[1:])
    con.commit()



print("SELECTING FROM TABLE")
statement = '''
            SELECT * FROM musician
            '''

res = cur.execute(statement)

print('-----------------')
n = [x[0] for x in res.description]
print (n)
print('-----------------')
for row in res : print(row)
print('-----------------')

#################################
#Create Instruments
#################################

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='instrument' ''')

if cur.fetchone()[0]==0:
    print("CREATING TABLE2")
    statement2 = '''
            CREATE TABLE instrument (
                          instrument_id text, 
                          type text, 
                          key text,
                          PRIMARY KEY(instrument_id)
                          );
            '''
    cur.execute(statement2)
    #inserting from csv
    file = open('instrument.csv')
    contents = csv.reader(file)
    contents = [x for x in contents]
    insert_records = "INSERT INTO instrument (instrument_id, type, key) VALUES(?,?,?)"
    cur.executemany(insert_records,contents[1:])
    con.commit()


print("SELECTING FROM TABLE2")
statement2 = '''
            SELECT * FROM instrument
            '''
res = cur.execute(statement2)
print('-----------------')
n = [x[0] for x in res.description]
print (n)
print('-----------------')
for row in res : print(row)
print('-----------------')
#################################
#Create Album
#################################

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='album' ''')
if cur.fetchone()[0]==0:
    print("CREATING TABLE3")
    statement3 = '''
            CREATE TABLE album (
                          name text, 
                          album_id text, 
                          date text,
                          type text,
                          PRIMARY KEY(album_id)
                          );
            '''
    cur.execute(statement3)
    #inserting from csv
    file = open('album.csv')
    contents = csv.reader(file)
    contents = [x for x in contents]
    insert_records = "INSERT INTO album (name, album_id, date, type) VALUES(?,?,?,?)"
    cur.executemany(insert_records,contents[1:])
    con.commit()

print("SELECTING FROM TABLE3")
statement3 = '''
            SELECT * FROM album
            '''
res = cur.execute(statement3)
print('-----------------')
n = [x[0] for x in res.description]
print (n)
print('-----------------')
for row in res : print(row)
print('-----------------')

#Now making relationships
# Album-Instrument
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='albumToinstrument' ''')
if cur.fetchone()[0]==0:
    print("CREATING TABLE albumToinstrument")
    statement3 = '''
            CREATE TABLE albumToinstrument (
                          album_id text,
                          instrument_id text,
                          PRIMARY KEY(album_id,instrument_id),
                          FOREIGN KEY(album_id) REFERENCES album,
                          FOREIGN KEY(instrument_id) REFERENCES instrument
                          );
            '''
    cur.execute(statement3)
    #inserting from csv
    file = open('album-instrument.csv')
    contents = csv.reader(file)
    contents = [x for x in contents]
    insert_records = "INSERT INTO albumToinstrument (album_id,instrument_id) VALUES(?,?)"
    cur.executemany(insert_records,contents[1:])
    con.commit()

print("SELECTING FROM albumToinstrument")
statement3 = '''
            SELECT * FROM albumToinstrument
            '''
res = cur.execute(statement3)
print('-----------------')
n = [x[0] for x in res.description]
print (n)
print('-----------------')
for row in res : print(row)
print('-----------------')

# Musician-Album

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='musicianToalbum' ''')
if cur.fetchone()[0]==0:
    print("CREATING TABLE musicianToalbum")
    statement3 = '''
            CREATE TABLE musicianToalbum (
                          ssn text,
                          album_id text,
                          PRIMARY KEY(ssn,album_id),
                          FOREIGN KEY(album_id) REFERENCES album,
                          FOREIGN KEY(ssn) REFERENCES musician
                          );
            '''
    cur.execute(statement3)
    #inserting from csv
    file = open('musician-album.csv')
    contents = csv.reader(file)
    contents = [x for x in contents]
    insert_records = "INSERT INTO musicianToalbum (ssn,album_id) VALUES(?,?)"
    cur.executemany(insert_records,contents[1:])
    con.commit()

print("SELECTING FROM musicianToalbum")
statement3 = '''
            SELECT * FROM musicianToalbum
            '''
res = cur.execute(statement3)
print('-----------------')
n = [x[0] for x in res.description]
print (n)
print('-----------------')
for row in res : print(row)
print('-----------------')
print("###############################################")

cur.close()
con.close()