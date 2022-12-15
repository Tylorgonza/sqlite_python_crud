import sqlite3
import os.path
import csv
import argparse


print('SQLite version:')
print(sqlite3.version)
con = sqlite3.connect('CSCI4333.db')
cur = con.cursor()

parser = argparse.ArgumentParser(description="add or delete records from specified table in database")
#parser.add_argument('--[add][delete]',metavar='operation',type=str,help="enter either operation --add or --delete")
group = parser.add_mutually_exclusive_group()
group.add_argument("--add",action='store_true',help="adding a record to specified album")
group.add_argument("--delete",action='store_true',help="delete from the specified album this record")
parser.add_argument('--table',metavar='table',type=str,required=True, help = "enter table name")
parser.add_argument('--record',metavar='record',type=str,required=True,help= "enter the record you want to act on")
args = parser.parse_args()

table_name = args.table
record = args.record
record = [x for x in record.split(',')]


print("---------------")
if args.add:
    print("add: " + str(args.add))
    if args.table == "album":
        print("ALBUM")
        query = "INSERT INTO album (name, album_id, date, type) VALUES(?,?,?,?)"
        contents = record
        cur.executemany(query,[contents])
        #query2 = "INSERT INTO albumToinstrument(album_id,instrument_id) VALUES(?,?)"
        #contents2 = [contents[1]]
        con.commit()
    elif args.table == "musician":
        query = "INSERT INTO musician (num, street, str_type, name, ssn) VALUES(?,?,?,?,?)"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
    elif args.table == "instrument":
        query = "INSERT INTO instrument (instrument_id, type, key) VALUES(?,?,?)"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
    elif args.table == "albumToinstrument":
        query = "INSERT INTO albumToinstrument (album_id,instrument_id) VALUES(?,?)"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
    elif args.table == "musicianToalbum":
        query = "INSERT INTO musicianToalbum (ssn,album_id) VALUES(?,?)"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
elif args.delete:
    print("delete: "+ str(args.delete))
    if args.table == "album":
        print("ALBUM")
        query = "DELETE FROM album WHERE name = ? AND album_id = ? AND date = ? AND type = ?"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
    elif args.table == "musician":
        query = "DELETE FROM musician WHERE num = ? AND street = ? AND str_type = ? AND name = ? AND ssn = ?"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
    elif args.table == "instrument":
        query = "DELETE FROM instrument WHERE instrument_id = ? AND type = ? AND key = ?"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
    elif args.table == "albumToinstrument":
        query = "DELETE FROM albumToinstrument WHERE album_id = ? AND instrument_id = ?"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
    elif args.table == "musicianToalbum":
        query = "DELETE FROM musicianToalbum WHERE ssn = ? AND album_id = ?"
        contents = record
        cur.executemany(query,[contents])
        con.commit()
else:
    print("please use --add or --delete")



print("this is our table name: " + table_name)
print("this is our record: " + str(record))



#word = "ty,019,2022,MB"
#word = [x for x in word.split(",")]
#print(word)


con.commit()
con.close()